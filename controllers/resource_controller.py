from flask import request, jsonify
from config.db import db
from bson import json_util,ObjectId
import sys
import os

# Add the parent_folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

task_collection = db['tasks']
resource_collection = db['resource']

def get_resource():
    resource = list(resource_collection.find())
    serialized_data = json_util.dumps(resource)  
    return jsonify(serialized_data),200

def create_resource():
    data = request.json
    resource_name = data.get('resource_name')
    task_assigned = data.get('task_assigned')
    
    task = task_collection.find_one({'task_name': task_assigned})
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    resource_data = {
        'resource_name': resource_name,
        'task_assigned': task_assigned
    }

    resource_id = resource_collection.insert_one(resource_data).inserted_id
    return jsonify({"message": "Resource created successfully", "resource_id": str(resource_id)}), 201

   
   
def delete_resource(resource_id):
    deleted_resource = resource_collection.find_one_and_delete({"_id": ObjectId(resource_id)})
    if not deleted_resource:
        return jsonify({"error": "Resource not found"}), 404
    return jsonify({"message": "Resource deleted successfully"}), 200

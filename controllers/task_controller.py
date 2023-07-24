from flask import request, jsonify
from config.db import db
from bson import json_util,ObjectId
import sys
import os

# Add the parent_folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


def create_task():
    data = request.json
    task_name = data.get('task_name')
    status = data.get('status')
    project_name = data.get('project_name')
    project = db.projects.find_one({'project_name': project_name})
    if not project:
        return jsonify({'message': 'project not found'}), 404

    task_data = {
        'task_name': task_name,
        'status': status,
        'project_name':project_name,
        'project_id': project['_id'],
    }

    task_id = db.tasks.insert_one(task_data).inserted_id
    return jsonify({'message': 'Task created successfully'}), 201

def getAll_tasks():
    task_collection = db['tasks']
    tasked = list(task_collection.find())
    serialized_data = json_util.dumps(tasked)  
    return jsonify(serialized_data),200

def delete_task(task_id):
    task_collection= db['tasks']
    task = task_collection.delete_one({"_id":ObjectId(task_id)})
    if task.deleted_count>0:
        return jsonify({"message":"task deleted successfully"}),200
    else:
        return jsonify({"message":"task not found"}),404
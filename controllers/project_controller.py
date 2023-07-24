from flask import request, jsonify
from bson import ObjectId,json_util
import sys
import os

# Add the parent_folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from config.db import db

# //creating project
def create_project():
    data = request.json
    project_name = data.get('project_name')
    status = data.get('status')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    portfolio_manager_name = data.get('portfolio_manager_name') 

    if not project_name or not status or not start_date or not end_date or not portfolio_manager_name:
        return jsonify({'message': 'Missing required fields'}), 400

    # Get the Portfolio Manager ID based on the provided email
    portfolio_manager = db.portfolio_Manager.find_one({'name': portfolio_manager_name})
    if not portfolio_manager:
        return jsonify({'message': 'Portfolio Manager not found'}), 404

    project_data = {
        'project_name': project_name,
        'status': status,
        'start_date': start_date,
        'end_date': end_date,
        'portfolio_manager_id': portfolio_manager['_id'],
    }

    project_id = db.projects.insert_one(project_data).inserted_id
    return jsonify({'message': 'Project created successfully'}), 201

# //getting projects
def get_all_projects():
    projects = list(db.projects.find({}))
    serialized_data = json_util.dumps(projects) 
    return jsonify(serialized_data), 200

def delete_project_byId(project_id):
    project_collection = db['projects']
    project = project_collection.delete_one({"_id":ObjectId(project_id)})

    if project.deleted_count>0:
        return jsonify({"message":"project deleted successfully"}),200
    else:
        return jsonify({"message":"project not found"}),404
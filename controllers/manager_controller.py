from flask import request, jsonify
from bson import ObjectId
import sys
import os

# Add the parent_folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from config.db import db

#creating new portfolio managers
def create_managers():
    data = request.json
    img=data.get('img')
    name = data['name']
    status = data['status']
    role = data['role']
    bio = data['bio']
    start_date = data['start_date']

    manager_collection = db['portfolio_Manager']
    manager_data = {
        "img": img,
        'name':name,
        'status': status,
        'role': role,
        'bio': bio,
        'start_date': start_date
    }
    manager_id = manager_collection.insert_one(manager_data).inserted_id

    return jsonify({"message":"New Portfolio Manager created successfully"})

#getting all portfolio managers
def getAll_managers():
    manager_collection = db['portfolio_Manager']
    managers = list(manager_collection.find())

    # Convert ObjectId instances to strings
    for manager in managers:
        manager["_id"] = str(manager["_id"])

    return jsonify(managers),200

#getting particular manager with specific id
def get_managers_byId(manager_id):
    manager_collection = db['portfolio_Manager']
    manager = manager_collection.find_one({"_id":ObjectId(manager_id)})

    manager["_id"] = str(manager["_id"])

    if manager:
        return jsonify(manager),200
    else:
        return jsonify({"message":"Portfolio Manager not found"}),404
    
#updating portfolio managers
def update_managers_byId(manager_id):
    data = request.json
    name = data['name']
    status = data['status']
    role = data['role']
    bio = data['bio']
    start_date = data['start_date']

    manager_collection = db['portfolio_Manager']
    updated_manager = manager_collection.update_one({"_id":ObjectId(manager_id)},{"$set":{
        'name':name,
        'status': status,
        'role': role,
        'bio': bio,
        'start_date': start_date
    }})

    if updated_manager.matched_count>0:
        return jsonify({"message":"Portfolio manager updated Successfully"}),200
    else:
        return jsonify({"message":"Portfolio manager not found"}),404
    
#deleting portfolio managers
def delete_manager(manager_id):
    manager_collection = db['portfolio_Manager']
    deleted_manager = manager_collection.delete_one({"_id":ObjectId(manager_id)})

    if deleted_manager.deleted_count>0:
        return jsonify({"message":"Portfolio manager deleted successfully"}),200
    else:
        return jsonify({"message":"Portfolio manager not found"}),404
    

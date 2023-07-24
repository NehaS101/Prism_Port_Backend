from flask import request, jsonify
from config.db import db
import bcrypt
import jwt
from datetime import datetime, timedelta
from bson import json_util,ObjectId
import sys
import os

# Add the parent_folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

def signup():
    # Get the registration data from the request
    registration_data = request.get_json()
    name = registration_data.get("name")
    email = registration_data.get("email")
    password = registration_data.get("password")
    phone=registration_data.get("phone")
    address=registration_data.get("address")
    print(name,email,password,phone,address)
    # Check if the required fields are provided
    if not name or not email or not password:
        return jsonify({"message": "Missing required fields"})

    # Check if the user already exists in the database
    existing_user = db.users.find_one({"email": email})
    if existing_user:
        return jsonify({"message": "User already exists"})

    # Hash the password before storing it in the database
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Create a new user document
    new_user = {
        "name": name,
        "email": email,
        "password": hashed_password,
        "phone":phone,
        "address":address
        
    }

    # Insert the new user into the database
    db.users.insert_one(new_user)

    return jsonify({"message": "Registration successful"})
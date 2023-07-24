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

def login():
    # Get the login data from the request
    login_data = request.get_json()
    email = login_data.get("email")
    password = login_data.get("password")

    # Check if the required fields are provided
    if not email or not password:
        return jsonify({"message": "Missing required fields"})

    # Check if the user exists in the database
    user = db.users.find_one({"email": email})
    if not user:
        return jsonify({"message": "Invalid email or password"})

    # Check if the password is correct
    if not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
        return jsonify({"message": "Invalid email or password"})

    # Generate a JWT token with the user's email and an expiration time
    token_payload = {
        "email": user["email"],
        "exp": datetime.utcnow() + timedelta(days=1)  # Token expiration time (1 day in this example)
    }
    token = jwt.encode(token_payload, "Atithi", algorithm="HS256")

    # Get the user's id
    user_id = str(user["_id"])

    # Return the response with the id and token included
    return jsonify({"message": "Login successful", "name": user["name"], "id": user_id, "token": token})
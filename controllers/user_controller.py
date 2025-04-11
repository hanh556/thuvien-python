from flask import request, jsonify, current_app
from models.user_model import UserModel

def get_users():
    users = UserModel.get_all()
    return jsonify(users)

def add_user():
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    result = UserModel.insert_user(name, age)
    return jsonify(result)

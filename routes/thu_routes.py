from flask import Blueprint
from controllers.user_controller import get_users, add_user

user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/users', methods=['GET'])
def get_all_users():
    return get_users()

@user_routes.route('/users', methods=['POST'])
def create_user():
    return add_user()

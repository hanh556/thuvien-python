from flask import current_app

class UserModel:
    @staticmethod
    def get_all():
        mongo = current_app.mongo
        users = mongo.db.users.find()
        return [{'_id': str(u['_id']), 'name': u['name'], 'age': u['age']} for u in users]

    @staticmethod
    def insert_user(name, age):
        mongo = current_app.mongo
        user = {"name": name, "age": age}
        mongo.db.users.insert_one(user)
        return {"message": "User added", "user": user}

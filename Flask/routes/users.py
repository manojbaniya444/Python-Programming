from flask import Blueprint, jsonify, request
from data import users

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
def get_users():
  return jsonify(users), 200

@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
  user = next((u for u in users if u["id"] == user_id), None)
  
  if not user:
    return jsonify({ "error": "User not found" }), 404
  
  return jsonify(user), 200

@users_bp.route("/", methods=["POST"])
def create_user():
  data = request.get_json()
  new_user = {
    "id": len(users) + 1,
    "name": data["name"],
    "email": data["email"]
  }
  users.append(new_user)
  return jsonify(new_user), 201

@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
  user = next((u for u in users if u["id"] == user_id), None)
  if not user:
    return jsonify({"error": "User not found"}), 404
  
  data = request.get_json()
  user.update(data)
  return jsonify(user), 200

@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
  global users
  users = [u for u in users if u["id"] != user_id]
  return jsonify({"message": "User deleted"}), 200

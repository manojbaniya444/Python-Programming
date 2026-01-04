from flask import Blueprint, request, jsonify

from app.database.connection import db

def get_users_repo():
  print("get the users repo")
  
users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
  """Get all the users"""
  try:
    # load the users repo
    return {
      "data": [{"id": 1, "test": "test the data"}]
    }
  except Exception as e:
    return jsonify({"error": "failed to retrieve users data"}), 500
  

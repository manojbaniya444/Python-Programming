from flask import request, jsonify
from functools import wraps

def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = request.headers.get("Authorization")
    if not token or token != "Bearer dummy_token":
      return jsonify({"error": "Unauthorized"}), 401
    return f(*args, **kwargs)
  return decorated
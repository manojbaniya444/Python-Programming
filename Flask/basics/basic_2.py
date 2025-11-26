from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

def require_auth(func):
  wraps(func)
  def authenticate(*args, **kwargs):
    print("Authenticating the request")
    auth_header = request.headers.get("Authorization")
    if not auth_header:
      return jsonify({"error": "Unauthorized"}), 403
    return func(*args, **kwargs)
  return authenticate

@app.route("/", methods=["GET"])
@require_auth
def test():
  return "Test", 200

if __name__ == "__main__":
  app.run(debug=True)
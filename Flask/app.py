from flask import Flask, jsonify
from config import Config

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  
  # Register the blueprints
  
  # Add the Api
  @app.route("/")
  def home():
    return jsonify({
      "message": "Welcome to Flask Learning API"
    }), 200
    
  @app.errorhandler(404)
  def not_found(e):
    return jsonify({"error": "Resource not found"}), 404
  
  @app.errorhandler(500)
  def server_error(e):
    return jsonify({"error": "Something went wrong"}), 500
  
  return app

if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)
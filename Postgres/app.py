from flask import Flask, jsonify
from app.config import Config
from app.database.connection import db
import logging

logger = logging.getLogger(__name__)

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  
  # register the api route
  
  # add the api
  @app.route("/")
  def index():
    return jsonify({
      "message": "the server is up"
    })
    
  @app.errorhandler(404)
  def not_found(e):
    return jsonify({"error": "Requested resource not found"}), 404
  
  @app.errorhandler(500)
  def server_error(e):
    return jsonify({"error": "something went wrong"}), 500
  
  return app

if __name__ == "__main__":
  app = create_app()
  # init the database
  try:
    db.init_app(app)
    logger.info("Database init success")
  except Exception as e:
    logger.error("Error setting up the database", e)
  
  app.run(debug=True)
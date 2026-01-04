import os
from pathlib import Path
from dotenv import load_dotenv

basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir / '.env')

# Define the Configuration to be used in the project
class Config:
  """Base Configuration"""
  SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')

  # Database Configuration
  DB_HOST = os.getenv('DB_HOST')
  DB_PORT = os.getenv('DB_PORT')
  DB_NAME = os.getenv('DB_NAME')
  DB_USER = os.getenv('DB_USER')
  DB_PASSWORD = os.getenv('DB_PASSWORD')

  # Connection Pool Settings
  DB_POOL_SIZE = int(os.getenv('DB_POOL_SIZE', '10'))
  DB_MAX_OVERFLOW = int(os.getenv('DB_MAX_OVERFLOW', '20'))
  DB_POOL_TIMEOUT = int(os.getenv('DB_POOL_TIMEOUT', '30'))
  DB_POOL_RECYCLE = int(os.getenv('DB_POOL_RECYCLE', '3600'))
  
  # Application
  FLASK_ENV = os.getenv('FLASK_ENV', 'development')
  DEBUG = False
  
  # Logging
  LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

  @property
  def DATABASE_URI(self):
    return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
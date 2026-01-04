import psycopg2
from psycopg2 import pool, extras
from contextlib  import contextmanager
import flask
import logging

logger = logging.getLogger(__name__)

class DatabaseConnection:
  """
  Manages PostgreSQL connection pool for the application.
  Uses the psycopg2 for raw SQL operations with proper connection pooling
  """
  def __init__(self, app=None):
    self.pool = None
    if app is not None:
      self.init_app(app)
  
  def init_app(self, app):
    """Initialize the database connection pool"""
    try:
      self.pool = pool.ThreadedConnectionPool(
        minconn=1,
        maxconn=app.config['DB_POOL_SIZE'],
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        database=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        cursor_factory=extras.RealDictCursor # access the data to the rows as the dict and not indices
      )
      logger.info("Database connection pool created successfully")
      # in the flask cleanup in the application context finish
      app.teardown_appcontext(self.close_connection)
    
    except psycopg2.Error as e:
      logger.error(f"Failed to create connection pool: {e}")
      raise
    
  def get_connection(self):
    """Get a connection from the pool"""
    if 'db_conn' not in flask.g: # application global context
      if self.pool is None:
        raise RuntimeError("Database pool not initialized")
      flask.d.db_conn = self.pool.getconn()
      logger.debug("New connection acquired from pool")
    
    return flask.g.db_conn
  
  def close_connection(self, exception=None):
    """Return connection to the pool"""
    conn = flask.g.pop('db_conn', None)
    if conn is not None:
      if exception:
        conn.rollback()
        logger.warning("Query rolled back due to exception")
      self.pool.putconn(conn)
      logger.debug("Connection returned to pool")
      
  @contextmanager
  def get_cursor(self, commit=True):
    """Context managaer for getting a cursor"""
    conn = self.get_connection()
    cursor = conn.cursor()
    
    try:
      yield cursor
      if commit:
        conn.commit()
    except Exception as e:
      conn.rollback()
      logger.error("Database Error: ", e)
      raise
    finally:
      cursor.close()
      
  @contextmanager
  def transaction(self):
    """Context manager for explicit transaction control"""
    conn = self.get_connection()
    cursor = conn.cursor()
    
    try:
      yield cursor
      conn.commit()
      logger.debug("Transaction commited")
    except Exception as e:
      conn.rollback()
      logger.error("Transaction roll back", e)
      raise
    finally:
      cursor.close()
      
  def execute_query(self, query, params=None, fetch_one=False, fetch_all=True):
    """Execute a query and return results"""
    with self.get_cursor() as cur:
      cur.execute(query, params)
      
      # return row one
      if fetch_one:
        return cur.fetchone()
      # return row all
      elif fetch_all:
        return cur.fetchall()
      return None
    
  def close_pool(self):
    """Close all connections in pool"""
    if self.pool:
      self.pool.closeall()
      logger.info("Connection pool closed")
      
# database connection instance
db = DatabaseConnection()
from psycopg2 import pool
import config


class Database:
    __connection_pool = None

    @classmethod
    def initialise(cls):
        POSTGRES_URL = config.CONFIG['postgresUrl']
        POSTGRES_PORT = config.CONFIG['postgresPort']
        POSTGRES_USER = config.CONFIG['postgresUser']
        POSTGRES_PASS = config.CONFIG['postgresPass']
        POSTGRES_DB = config.CONFIG['postgresDb']
        Database.__connection_pool = pool.ThreadedConnectionPool(1,100, user = POSTGRES_USER, password= POSTGRES_PASS,host = POSTGRES_URL, port=POSTGRES_PORT,database=POSTGRES_DB)
        

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()
    
    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)
    
    @classmethod
    def close_all_connections(cls, connection):
        Database.__connection_pool.closeall()


class ConnectionPool:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
Database.initialise()

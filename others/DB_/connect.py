import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError, DatabaseError

# Load environment variables from a .env file
load_dotenv()
conn = None


def db_credentials():
    try:
        credentials = {
            'host': os.getenv('host'),
            'port': os.getenv('port'),
            'user': os.getenv('user'),
            'password': os.getenv('password'),
            'dbname': os.getenv('dbname')
        }
    except Exception as e:
        print("DB credentials not found / Wrong credentials")
        return None
    return credentials


def get_connect():
    credentials = db_credentials()
    if credentials is None:
        return None, False
    # conn  = None
    # if conn:
    #     print(conn)
    #     return conn, True

    else:
        try:
            conn = psycopg2.connect(
                host=credentials['host'],
                port=credentials['port'],
                user=credentials['user'],
                password=credentials['password'],
                dbname=credentials['dbname']
            )
            
            with conn.cursor() as cursor:
                cursor.execute("SELECT version();")
                db_version = cursor.fetchone()
                print(f"Connected to PostgreSQL database:\n{db_version[0]}")
            return conn, True

        except OperationalError as e:
            return f"Operational error: {e}", False
        except DatabaseError as e:
            return f"Database error: {e}", False
        except Exception as e:
            return f"Unexpected error: {e}", False

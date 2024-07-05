import psycopg2
from psycopg2 import sql

# Connection parameters
host = "aws-0-ap-south-1.pooler.supabase.com"
port = "6543"
user = "postgres.irnkwhjszpphltqunuib"
password = "Sirius.@.1718:8"
dbname = "postgres"

try:
    # Establish the connection
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        dbname=dbname
    )
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Execute a simple SQL query to test the connection
    cursor.execute("SELECT version();")
    
    # Fetch the result of the query
    db_version = cursor.fetchone()
    
    # Print the result
    print(f"Connected to PostgreSQL database:\n{db_version}")
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error connecting to the database: {e}")

from flask import Flask, jsonify
import os
from dotenv import load_dotenv
from DB_.connect import db_credentials, get_connect
from DB_.create_table import create_table

load_dotenv()

app = Flask(__name__)
conn = None
is_connected = False









@app.route('/login', methods=['GET'])
def login():
    global conn, is_connected
    try:
        conn, is_connected = get_connect()
        if is_connected:
            return jsonify({"message": "Successfully logged in and connected to database"})
        else:
            return jsonify({"message": "Connection failed"})
    except Exception as e:
        print(e)
        return jsonify({"error": f"Connection error: {str(e)}"})







@app.route('/create_table', methods=['GET'])
def create_table_endpoint():
    global conn, is_connected
    if is_connected:
        try:
            create_table(conn, "words")
            return jsonify({"message": "Table created successfully"})
        except Exception as e:
            return jsonify({"error": f"Table creation error: {str(e)}"})
    else:
        return jsonify({"message": "Not connected to database"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)

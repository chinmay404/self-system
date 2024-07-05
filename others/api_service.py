from fastapi import FastAPI
import os
from dotenv import load_dotenv






#USER IMPORT'S
from DB_.connect import db_credentials, get_connect  # Assuming DB_.connect defines these functions
from DB_.creat_table import create_table   # Assuming DB_.connect defines these functions





load_dotenv()
app = FastAPI()
conn = None
is_connected = False



@app.get("/login")
async def login():
    try:
        conn, is_connected = get_connect()
        print(conn,is_connected)
        if is_connected:
            return {"message": "Successfully Loggedin and connected to database"}
        else:
            return {"message": "Connection failed"}

    except Exception as e:
        return {"error": f"Connection error: {str(e)}"}



@app.get("/creat_table")
def creat_table():
    print(conn,is_connected)
    if is_connected:
        try:
            create_table(conn,"words")
            return {"message": "Table created successfully"}
        except Exception as e:
            return {"error": f"Table creation error: {str(e)}"}
    else:
        return {"message": "Not connected to database"}







if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_service:app", host="0.0.0.0", port=8000)

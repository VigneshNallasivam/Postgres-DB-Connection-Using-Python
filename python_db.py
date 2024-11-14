import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def connect_to_db():
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
    
    table = 'items'
    
    connection_url = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"
    connection = psycopg2.connect(connection_url)
    
    cursor = connection.cursor()
    
    query = f"""SELECT * FROM {table}"""
    cursor.execute(query)
    
    rows = cursor.fetchall()
    print(f"The data from {table} are as follows : ",rows)
    
    cursor.close()
    connection.close()
    
connect_to_db()
    

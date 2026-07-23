import os
import pymysql 
from dotenv import load_dotenv
from pymysql.cursors import DictCursor

def obtener_conexion()
return pymysql.connect(
    Host="db_host",
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("my_app"),
    cursorclass=DictCursor
)
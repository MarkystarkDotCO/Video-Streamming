from flask import Blueprint, jsonify
#import psycopg2
import pyodbc 


api_bp = Blueprint('api', __name__)

####### test API success
@api_bp.route('/')
def index():
    server = 'webse.database.windows.net'
    database = 'videostreaming'
    username = 'webse001'
    password = 'vajajava+25%'   
    driver= '{ODBC Driver 17 for SQL Server}'
    i = "HIIII"
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM testDB")
            row = cursor.fetchone()
            while row:
                print (str(row[0])+" ")
                i= str(row[0])
                row = cursor.fetchone()
    return i
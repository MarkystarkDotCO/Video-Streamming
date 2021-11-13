from flask import Blueprint, jsonify, request
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

########## write member
@api_bp.route('/write-member/<id>/<fname>/<mname>/<lname>/<username>/<password>/<expiredate>/<displayname>/<email>/<membertype>')
def write_member(id,fname,mname,lname,username,password,expiredate,displayname,email,membertype):
    server = 'webse.database.windows.net'
    database = 'videostreaming'
    username = 'webse001'
    password = 'vajajava+25%'   
    driver= '{ODBC Driver 17 for SQL Server}'
    i = "HIIII"
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO members(member_id, member_firstname, member_midname, member_lastname, member_username, member_password, member_expire_date, member_displayname, membertype_email, membertype_id) VALUES("+id+","+fname+","+mname+","+lname+","+username+","+password+","+expiredate+","+displayname+","+email+","+membertype+")")
            cursor.commit()
            #cursor.execute("select * from members;")
            row = cursor.fetchone()
            while row:
                print (str(row[0])+" ")
                i= str(row[0])
                row = cursor.fetchone()
    return id
######read members
@api_bp.route('/read-member')
def read_member():
    server = 'webse.database.windows.net'
    database = 'videostreaming'
    username = 'webse001'
    password = 'vajajava+25%'   
    driver= '{ODBC Driver 17 for SQL Server}'
    i = "HIIII"
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM members")
            row = cursor.fetchone()
            while row:
                print (str(row[row])+" ")
                i= str(row[0])
                row = cursor.fetchone()
    return i
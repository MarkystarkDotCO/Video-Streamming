from flask import Blueprint, render_template
import cgi

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/')
def login():
    return render_template('login.html')

@auth_bp.route('/abc')
def dog():
    return "HELLO"
#ID = cgi.FieldStorage()
 #   id =  ID.getvalue('firstname')
  #  print(id)
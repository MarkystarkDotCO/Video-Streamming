
from flask import Blueprint
import pyodbc
from flask.templating import render_template
#git test

main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main_bp.route('/', methods = ['POST', 'GET'])
def index():
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-NG2KJDA\SQLEXPRESS;'
                              'Database=suki;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('SELECT Url FROM Description')
        data=cursor.fetchall()
        return render_template('home.html',data=data)

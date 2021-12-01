
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
        
        cursor.execute('SELECT TOP 1 * FROM Description order by NEWID()')
        BgImg=cursor.fetchone()
        
       #poppulation
        cursor.execute('SELECT TOP 4 * FROM Description order by NEWID()')
        pop1=cursor.fetchall()
        
        cursor.execute('SELECT TOP 4 * FROM Description order by NEWID()')
        pop2=cursor.fetchall()
        
        cursor.execute('SELECT TOP 4 * FROM Description order by NEWID()')
        pop3=cursor.fetchall()
        
        #Action
        cursor.execute('SELECT TOP 4 * FROM Description order by NEWID()')
        act1=cursor.fetchall()
        
        cursor.execute('SELECT TOP 4 * FROM Description order by NEWID()')
        act2=cursor.fetchall()
        
        cursor.execute('SELECT TOP 4 * FROM Description order by NEWID()')
        act3=cursor.fetchall()
     
        return render_template('homes.html',BgImg=BgImg,pop=pop1,pop2=pop2,pop3=pop3,act1=act1,act2=act2,act3=act3)

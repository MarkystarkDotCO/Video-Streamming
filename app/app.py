from flask import Flask
#from example_blueprint import example_blueprint
from auth.auth import auth_bp
from api.api import api_bp
from payment.payment import payment_bp
from main.main import main_bp

app = Flask(__name__)
#app.register_blueprint(example_blueprint)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(payment_bp, url_prefix='/payment')
app.register_blueprint(main_bp, url_prefix='/')

if __name__ == '__main__':
  app.run(
  #host='0.0.0.0', 
  #port=80, 
  debug=True)

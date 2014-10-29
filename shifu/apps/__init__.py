
from flask import Flask 
from config import Config
from flask import Blueprint

app = Flask(__name__)

#configuration
app.config.from_object(Config)

# another way of configuration
#app.config['CSRF_ENABLED'] = True
#app.config['SECRET_KEY'] = 'some_Secret_key_XtksCaSEdc98'

# blueprint for master of application
master = Blueprint('master',__name__,template_folder='templates',static_folder='static')
from views import *

from users import users
#from users import views

#registering all blueprints
app.register_blueprint(master)
app.register_blueprint(users)
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_script import Manager
from flask_login import LoginManager

from app import login



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login.login_view = "login"


from app import routes, models


# manager = Manager

#login = LoginManager(app)
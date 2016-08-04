from flask import Flask
from config import basedir
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from flablo import views, models

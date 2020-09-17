from flask import Flask
from config import Config  # Config class we have created
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)  # Import configuration variables from our class
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'  # Tell loginmanager our view function to login

from my_package import routes

# Routes are different URLs that the application implements
# Handlers for the application routes are written as view functions
# View functions are mapped to one or more route URLs
# This gives Flask the logic to execute when a client requests a UR:

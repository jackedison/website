from flask import Flask
from config import Config  # Config class we have created
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging
import os
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
app.config.from_object(Config)  # Import configuration variables from our class
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'  # Tell loginmanager our view function to login

from my_package import routes, models, errors

# Routes are different URLs that the application implements
# Handlers for the application routes are written as view functions
# View functions are mapped to one or more route URLs
# This gives Flask the logic to execute when a client requests a UR:


# Log errors
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/errors.log', maxBytes=10240,
                                       backupCount=10)

    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Website startup')

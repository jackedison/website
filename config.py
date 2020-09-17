import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Will use environment variable if set up else this string
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'potato-carrot-pomme'

    # If database_url environment variable is setup take from that
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'website_data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Don't signal to Flask every change
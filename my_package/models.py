from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin  # Default parameters for flask_login user
from my_package import login  # For user loader
from my_package import db
from hashlib import md5  # To hash for Gravatar


# Create a class for our user's data using db instance of SQLAlchemy
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # High level view of relationship between users and posts
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        # Convert input password to the hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        # hash for random img
        # d variable is for unregistered users random gemoetric design
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Create a class for posts linked to user_id
# Timestamped index to help retrieve in chronolocial order
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign Key
    # Note user has lowercase name as SQLAlchemy automatically uses lowercase

    def __repr__(self):
        return '<Post {}'.format(self.body)


# Create SQLAlchemy Projects mnodel for instance
class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    img_path = db.Column(db.String(60))  # Path to img
    url_to_link = db.Column(db.String(60))

    # Could also add:
    # language coded in (list). Thinking bullet points of colour coded in html
    # frameworks/packages used (list)
    # category (finance, game solving, other?) Then can filter for with html
    # link: type (github, website) and link

    # For a list we want a second table. We would then join on project id.
    # id | Project id | Language used
    # 1 | 1 | Python
    # 2 | 1 | HTML
    # 3 | 1 | CSS
    # 4 | 2 | Python



    def __repr__(self):
        return '<Project {}'.format(self.title)

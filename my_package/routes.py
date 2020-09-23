from flask import render_template, flash, redirect, url_for
from my_package import app
from my_package.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from flask_login import login_required  # @login_required decorator if needed
from my_package.models import User, Post, Projects
from my_package import db
from my_package.forms import RegistrationForm, AboutMeForm
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime

# This imports the Flask app


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'Luke'},
            'body': 'Welcome to day 1 of the website!'
        },
        {
            'author': {'username': 'Sam'},
            'body': 'Maybe we should add some CSS...'
        }
    ]
    # Return HTML code from template and rendered variables
    return render_template('index.html', title='Home', posts=posts)


# @ decorators associate the URLs / and /index to this function
# Recall decorators mofidy the function that follow it

@app.route('/login', methods=['GET', 'POST'])  # Enable post request for forms
def login():
    if current_user.is_authenticated:  # If already logged in redirect off url
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():  # Validate validators attached to fields of form
        user = User.query.filter_by(username=form.username.data).first()
        # ^ .first() returns None if not valid user

        # Check if username and password are valid
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        # If all valid then login or redirect to page they were on before
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    # If form has some validation errors then return login page again
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    # Check if user exists else 404
    user = User.query.filter_by(username=current_user.username).first_or_404()
    form = AboutMeForm()
    if form.validate_on_submit():  # If form is valid and submit
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
    elif request.method == 'GET':  # If GET request for form then fill about_me
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', user=user, form=form)


@app.route('/user/<username>')  # Dynamic <username> variable
@login_required
def user(username):
    # Check if user exists else 404
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/projects')  # Page to share my projects
def projects():
    # Send html the db of my projects and thats about it?
    # Feed table name in as db then db.column in html
    projects = Projects.query.all()  # imported from models
    intro = '''
    Below are programming projects I have worked on in recent times. My 
    particular interests have been in market analysis, AI for game solving, 
    and some convenient tools. Click on images to go to project/github.'''
    return render_template('projects.html', intro=intro, projects=projects)


# Code to run on every user request (e.g. for user last seen timestamp)
@app.before_request
def before_request():
    if current_user.is_authenticated:  # if user is logged in
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

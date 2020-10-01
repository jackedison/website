from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms.validators import Length
from my_package.models import User


class LoginForm(FlaskForm):
    username = wtforms.StringField('Username', validators=[DataRequired()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    remember_me = wtforms.BooleanField('Remember Me')
    submit = wtforms.SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = wtforms.StringField('Username', validators=[DataRequired()])
    email = wtforms.StringField('Email', validators=[DataRequired(), Email()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    password2 = wtforms.PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = wtforms.SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:  # .first() returns None if don't exist
            raise ValidationError('Username already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already in use.')


class AboutMeForm(FlaskForm):
    about_me = wtforms.TextAreaField('About me')
    submit = wtforms.SubmitField('Submit')


class ProjectForm(FlaskForm):
    title = wtforms.StringField('Title')
    body = wtforms.TextAreaField('Body')
    img_path = wtforms.StringField('Image Path')
    url_to_link = wtforms.StringField('URL')
    key_project = wtforms.BooleanField('Key Project')

    choice_manip = lambda x: [(y, y) for y in x]
    language_list = ['Python', 'C++', 'Java', 'HTML', 'CSS', 'Javascript']
    language_list = choice_manip(language_list)
    languages = wtforms.SelectMultipleField(u'Languages', choices=language_list)

    package_list = ['numpy', 'pandas', 'matplotlib', 'keras']
    package_list = choice_manip(package_list)
    packages = wtforms.SelectMultipleField(u'Packages', choices=package_list)

    framework_list = ['Flask', 'React']
    framework_list = choice_manip(framework_list)
    frameworks = wtforms.SelectMultipleField(u'Frameworks', choices=framework_list)

    category_list = ['Finance', 'Monte Carlo', 'Games']
    category_list = choice_manip(category_list)
    categories = wtforms.SelectMultipleField(u'Categories', choices=category_list)

    submit = wtforms.SubmitField('Submit')
    delete = wtforms.SubmitField('Delete')
    new_project = wtforms.SubmitField('New Project')

from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
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

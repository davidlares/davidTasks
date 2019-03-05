# python class forms
from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms import validators
from wtforms.fields.html5 import EmailField

class LoginForm(Form):
    # attrs = inputs
    username = StringField('Username', [
        validators.length(min=4,max=50, message='Username out of range')
    ])
    password = PasswordField('Password',[
        validators.Required(message='Password required')
    ])

class RegisterForm(Form):
    # attrs
    username = StringField('Username', [
        validators.length(min=4,max=50)
    ])

    email = EmailField('Email', [
        validators.length(min=6,max=100),
        validators.Required(message='Email required'),
        validators.Email(message='Insert a valid email')
    ])

    password = PasswordField('Password', [
        validators.Required(message='Password required'),
        validators.EqualTo('confirm_password', message='Password do not match')
    ])

    confirm_password = PasswordField('Password confirmation')
    accept = BooleanField('', [
        validators.DataRequired()
    ])

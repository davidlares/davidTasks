# python class forms
from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators

class LoginForm(Form):
    # attrs = inputs
    username = StringField('Username', [
        validators.length(min=4,max=50, message='Username out of range')
    ])
    password = PasswordField('Password',[
        validators.Required()
    ])

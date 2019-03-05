# python class forms
from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms import validators
from wtforms.fields.html5 import EmailField

# custom validation
def custom_validator(form, field): # mandatory params
    if field.data == "david" or field.data == "davidlares":
        raise validators.ValidationError('That username is not allowed')

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
        validators.length(min=4,max=50),
        # adding custom validator
        custom_validator
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

    # validating from a method
    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('Username already in use')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('Email already in use')

    # overriding the validate method
    def validate(self):
        if not Form.validate(self): # actually run the previous validators before
            return False
        if len(self.password) < 3:
            self.password.errors.append('Password is too short')
            return False
        return True

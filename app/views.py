# blueprint class -> flask core
from flask import Blueprint
from flask import render_template, request, flash
# calling the classMethods
from .models import User
# bringing forms
from .forms import LoginForm, RegisterForm

page = Blueprint('page', __name__) # page (name of the context) (context of creation)

@page.app_errorhandler(404) # custom error page
def page_not_found(error):
    return render_template('errors/404.html'), 404 # second param is mandatory

@page.route('/')
def index():
    return render_template('index.html', title="Index")
    # return "Hello, World"

@page.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form) # with this param we can get form data
    if request.method == 'POST' and form.validate():
        print('New session created')
        print(form.username.data) # getting the value -> form.nameField.data
    return render_template('auth/login.html', title="Login", form=form)

@page.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user = User.create_element(form.username.data, form.password.data, form.email.data)
            flash("user created successfully")
    return render_template('auth/register.html', title='Register', form=form)

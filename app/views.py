# blueprint class -> flask core
from flask import Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, flash, redirect, url_for
# calling the classMethods
from .models import User
# bringing forms
from .forms import LoginForm, RegisterForm
from . import login_manager

page = Blueprint('page', __name__) # page (name of the context) (context of creation)

@login_manager.user_loader
def load_user(id): # for retrieving in the session (each request)
    return User.get_by_id(id)

@page.app_errorhandler(404) # custom error page
def page_not_found(error):
    return render_template('errors/404.html'), 404 # second param is mandatory

@page.route('/')
def index():
    return render_template('index.html', title="Index")
    # return "Hello, World"

@page.route('/login', methods=['GET','POST'])
def login():

    # validating auth
    if current_user.is_authenticated:
        return redirect(url_for('.tasks'))

    form = LoginForm(request.form) # with this param we can get form data
    if request.method == 'POST' and form.validate():
        print('New session created')
        print(form.username.data) # getting the value -> form.nameField.data

        # authentication
        user = User.get_by_username(form.username.data)
        if user and user.verify_password(form.password.data):
            login_user(user) # this generates a session
            flash("user logged in")
            login_user(user) # generating the session
            return redirect(url_for('.tasks'))
        else:
            flash('invalid user or password', 'error')

    return render_template('auth/login.html', title="Login", form=form)

@page.route('/register', methods=['GET', 'POST'])
def register():
    # validating auth
    if current_user.is_authenticated:
        return redirect(url_for('.tasks'))

    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user = User.create_element(form.username.data, form.password.data, form.email.data)
            flash("user created successfully")
    return render_template('auth/register.html', title='Register', form=form)

@page.route('/logout')
def logout():
    logout_user()
    flash('Log out successfully')
    return redirect(url_for('.login'))

# authenticated route
@page.route('/tasks')
@login_required
def tasks():
    return render_template('task/list.html', title='Tasks')

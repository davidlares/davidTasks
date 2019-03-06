# blueprint class -> flask core
from flask import Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, flash, redirect, url_for, abort
# calling the classMethods
from .models import User, Task
# bringing forms
from .forms import LoginForm, RegisterForm, TaskForm
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
@page.route('/tasks/<int:page>')
@login_required
def tasks(page=1, per_page=2):
    pagination = current_user.tasks.paginate(page, per_page=per_page) # get the tasks from the user
    task_list = pagination.items
    return render_template('task/list.html', title='Tasks', task_list=task_list, pagination=pagination, page=page)

@page.route('/tasks/new', methods=['GET','POST'])
@login_required
def new_tasks():
    form = TaskForm(request.form)
    if request.method == "POST":
        if form.validate():
            task = Task.create_element(form.title.data, form.description.data, current_user.id)
            if task:
                flash('Task created successfully', 'success')
    return render_template('task/new.html', title='Tasks', form=form)


@page.route('/tasks/edit/<int:task_id>', methods=['GET','POST'])
@login_required
def edit_tasks(task_id):
    task = Task.query.get_or_404(task_id) # get a record from a ID or show error
    # own edition
    if task.user_id != current_user.id:
        abort(404)

    form = TaskForm(request.form, obj=task) # auto fullfill form
    if request.method == "POST":
        if form.validate():
            task = Task.update_element(task.id,form.title.data, form.description.data)
            if task:
                flash('Task updated successfully', 'success')
    return render_template('task/edit.html', title='Edit Tasks', form=form)

@page.route('/tasks/show/<int:task_id>')
@login_required
def get_task(task_id):
    task = Task.query.get_or_404(task_id) # get a record from a ID or show error
    return render_template('task/show.html', title='Shot Tasks', task=task)

@page.route('/tasks/delete/<int:task_id>')
@login_required
def delete_tasks(task_id):
    task = Task.query.get_or_404(task_id) # get a record from a ID or show error
    # own edition
    if task.user_id != current_user.id:
        abort(404)

    # deleting record
    if Task.delete_element(task.id):
        flash('Task deleted successfully')
    return redirect(url_for('.tasks'))

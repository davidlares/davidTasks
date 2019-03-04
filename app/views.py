# blueprint class -> flask core
from flask import Blueprint
from flask import render_template

page = Blueprint('page', __name__) # page (name of the context) (context of creation)

@page.app_errorhandler(404) # custom error page
def page_not_found(error):
    return render_template('errors/404.html'), 404 # second param is mandatory

@page.route('/')
def index():
    return render_template('index.html', title="Index")
    # return "Hello, World"

# singleton pattern: unique instance
from flask import Flask

from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

mail = Mail()
db = SQLAlchemy()
csrf = CSRFProtect()
# bootstrap instance
bootstrap = Bootstrap()
login_manager = LoginManager()

from .views import page # getting the views from the page object
from .models import User, Task

def create_app(config):
    app.config.from_object(config) # we get the DEBUG = True attr

    csrf.init_app(app) # CSRF init
    bootstrap.init_app(app) # bootstrap init
    app.register_blueprint(page) # indicate the routes
    login_manager.init_app(app)
    login_manager.login_view = '.login' # URL for auth redirect (url_for)
    login_manager.login_message = 'Login required'
    mail.init_app(app) # initializing mail

    # like a try/catch
    with app.app_context():
        db.init_app(app) # db instance
        db.create_all() # create all tables

    return app

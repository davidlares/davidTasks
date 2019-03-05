# singleton pattern: unique instance
from flask import Flask

from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
csrf = CSRFProtect()
# bootstrap instance
bootstrap = Bootstrap()

from .views import page # getting the views from the page object
from .models import User

def create_app(config):
    app.config.from_object(config) # we get the DEBUG = True attr

    csrf.init_app(app) # CSRF init
    bootstrap.init_app(app) # bootstrap init
    app.register_blueprint(page) # indicate the routes

    # like a try/catch
    with app.app_context():
        db.init_app(app) # db instance
        db.create_all() # create all tables

    return app

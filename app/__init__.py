# singleton pattern: unique instance
from flask import Flask
from .views import page # getting the views from the page object
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# bootstrap instance
bootstrap = Bootstrap()

def create_app(config):
    app.config.from_object(config) # we get the DEBUG = True attr
    bootstrap.init_app(app) # bootstrap init
    app.register_blueprint(page) # indicate the routes
    return app

from app import create_app
from flask_script import Manager # server by instance
from config import config

config_class = config['development']

# singleton flask instance
app = create_app(config_class) # config class

if __name__ == "__main__":
    manager = Manager(app) # Manager instance (flask instance)
    manager.run()

# run the manager
# python manage.py runserver

from app import create_app
from flask_script import Manager, Shell # server by instance
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand # generating DB migrations
from app import db, User, Task

config_class = config['development']

# singleton flask instance
app = create_app(config_class) # config class
migrate = Migrate(app, db) # context and database

def make_shell_context():
    # return SQL models to use and context
    return dict(app=app, db=db, User=User, Task=Task)

if __name__ == "__main__":
    manager = Manager(app) # Manager instance (flask instance)
    # create commands for the shell
    manager.add_command('shell', Shell(make_context=make_shell_context))
    # migration
    manager.add_command('db', MigrateCommand)
    # test shell addon
    @manager.command
    def first_test():
        import unittest
        # external file
        tests = unittest.TestLoader().discover('tests') # py module
        unittest.TextTestRunner().run(tests)

        # run it like: python manage.py [test function]

    manager.run()

# run the manager
# python manage.py runserver

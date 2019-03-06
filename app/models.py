#only . because the __init__
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db

# users table representation
class User(db.Model, UserMixin): # Mixin for generating the Session
    __tablename__ = 'users'
    # attrs -> database columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    encrypted_password = db.Column(db.String(93), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    # belongs to relationship
    tasks = db.relationship('Task', lazy='dynamic')
    # object relationship with dynamic loading (for pagination)

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        self.encrypted_password = generate_password_hash(value) # encrypting password

    # everytime we print the Object, prints the username
    def __str__(self):
        return self.username

    @classmethod
    def create_element(cls, username, password, email):
        user = User(username=username, password=password, email=email)
        db.session.add(user) # adding to table
        db.session.commit() # confirm insertion

        return user

    def verify_password(self,password):
        return check_password_hash(self.encrypted_password, password)

    @classmethod
    def get_by_username(cls,username):
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls,email):
        return User.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls,id):
        return User.query.filter_by(id=id).first()

# generating tasks
class Task(db.Model):
    __tablename__ = 'tasks'
    # attrs
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text())
    # One to many Relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    # table column to be created with migration
    updated_at = db.Column(db.DateTime)

    @property
    def excerpt_description(self):
        if len(self.description) > 20:
            return self.description[0:19] + "..."
        return self.description

    @classmethod
    def create_element(cls, title, description, user_id):
        task = Task(title=title, description=description, user_id=user_id)
        db.session.add(task)
        db.session.commit()
        return task

    @classmethod
    def get_by_id(cls, id):
        return Task.query.filter_by(id=id).first()

    @classmethod
    def update_element(cls, id, title, description):
        task = Task.get_by_id(id)
        if task is None:
            return False
        # updating fields
        task.title = title
        task.description = description

        db.session.add(task)
        db.session.commit()
        return task

    @classmethod
    def delete_element(cls, id):
        task = Task.get_by_id(id)
        if task is None:
            return False

        db.session.delete(task)
        db.session.commit()
        return True

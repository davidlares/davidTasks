# global config
class Config:
    SECRET_KEY = 'mysecretkey' # this is for CSRF

# dev env config
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_tasks'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

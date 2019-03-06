# global config
class Config:
    SECRET_KEY = 'mysecretkey' # this is for CSRF

# dev env config
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_tasks'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '[email_account]@gmail.com' #assign permissions
    MAIL_PASSWORD = 'XXXXXXXXX' # or env variable

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

# global config
class Config:
    SECRET_KEY = 'mysecretkey' # this is for CSRF

# dev env config
class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

import os

class Config:

    # SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:12345@localhost/Pitch'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://CarineIzere:12345..@localhost/minutepitch'



    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
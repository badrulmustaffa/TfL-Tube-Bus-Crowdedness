"""Flask config class."""
from pathlib import Path


class Config(object):
    """ Sets the Flask base configuration that is common to all environment"""
    DEBUG = False
    SECRET_KEY = 'qpiwbSnk5ydJ_S4Eh1J1_Q'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATA_PATH = Path(__file__).parent.parent.joinpath("data")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(DATA_PATH.joinpath('example.sqlite'))

    # FOr photo upload
    UPLOADED_PHOTOS_DEST = Path(__file__).parent.joinpath("data").joinpath("user")


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True
    SQLALCHEMY_ECHO = True

# import secrets
# print(secrets.token_urlsafe(16))

"""Flask config class."""
from pathlib import Path


class Config(object):
    """ Sets the Flask base configuration that is common to all environment"""
    DEBUG = False
    SECRET_KEY = 'HD-WP-0q1EyscN_pBSQE0Q'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATA_PATH = Path('../data')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(DATA_PATH.joinpath('example.sqlite'))

    # FOr photo upload
    UPLOAD_PHOTOS_DEST = Path(__file__).parent.joinpath("static/img")


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

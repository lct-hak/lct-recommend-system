import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

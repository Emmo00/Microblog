from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI') or 'sqlite:///microblog.db'

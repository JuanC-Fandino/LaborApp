import os
from dotenv import load_dotenv
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True
    WTF_CSRF_ENABLED = False
    EXPLAIN_TEMPLATE_LOADING = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=5)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}

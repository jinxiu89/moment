import os


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    DEBUG = False
    TESTING = False


class Production(BaseConfig):
    pass


class Development(BaseConfig):
    DEBUG = True

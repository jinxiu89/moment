# from .config.config import config
# from .logger import register_logger
from config.config import config
from logger import register_logger

from flask import Flask

def create_app(deploy):
    register_logger() # 注册 日志
    app = Flask(__name__)
    app.config.from_object(config[deploy])
    return app

from flask import Flask
from ..config.config import config
from ..logger import register_logger

def create_app(deploy):
    register_logger() # 注册 日志
    app = Flask(__name__)
    app.config.from_object(config[deploy])
    return app

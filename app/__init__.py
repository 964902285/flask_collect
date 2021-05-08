"""
@File    : __init__.py
@Time    : 2021/4/23 16:14
@Author  : shroud.xu
@Description: 一个 ctrl c + v 工程师
@Email   : shroud.xu@cygia.com
@Software: PyCharm
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

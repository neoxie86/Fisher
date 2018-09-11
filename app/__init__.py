# -*- coding:utf-8 -*-
from flask import Flask
from app.models.book import db
__author__ = 'neo'
__time__ = '2018/9/6 10:38'


def create_app():
    app = Flask(__name__)
    # 载入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
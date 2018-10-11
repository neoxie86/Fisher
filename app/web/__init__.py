# -*- coding:utf-8 -*-
from flask import Blueprint,render_template
__author__ = 'neo'
__time__ = '2018/9/6 10:38'

web = Blueprint('web',__name__)

@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html')

from app.web import book
from app.web import user
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
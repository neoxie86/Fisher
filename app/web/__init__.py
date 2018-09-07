# -*- coding:utf-8 -*-
from flask import Blueprint
__author__ = 'neo'
__time__ = '2018/9/6 10:38'

web = Blueprint('web',__name__)

from app.web import book
from app.web import user
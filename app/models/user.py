# -*- coding:utf-8 -*-
from app.models.base import db,Base
from sqlalchemy import Column,Integer,String,Boolean,Float
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager


__author__ = 'neo'
__time__ = '2018/9/12 11:00'

class User(UserMixin,Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    nickname = Column(String(24),nullable=False)
    _password = Column('password',String(128),nullable=False)
    phone_number = Column(String(18),unique=False)
    email = Column(String(50),unique=True,nullable=False)
    confirmed = Column(Boolean,default=False)
    beans = Column(Float,default=0)
    send_counter = Column(Integer,default=0)
    receive_counter = Column(Integer,default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    def check_password(self,raw):
        return check_password_hash(self._password,raw)

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
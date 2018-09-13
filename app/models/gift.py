# -*- coding:utf-8 -*-
from sqlalchemy import Column,Integer,Boolean,String,ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import db
__author__ = 'neo'
__time__ = '2018/9/12 11:00'

class Gift(db.Model):
    id = Column(Integer,primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    #数据库中并没有book，直接用接口返回的数据
    # book = relationship('Book')
    # bid = Column(Integer,ForeignKey('book.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean,default=False)

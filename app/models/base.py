# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,SmallInteger
__author__ = 'neo'
__time__ = '2018/9/12 11:01'


db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    # create_time = Column('create_time',Integer)
    status = Column(SmallInteger,default=1)

    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != 'id':
                setattr(self,key,value)

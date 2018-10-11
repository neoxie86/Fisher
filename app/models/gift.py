# -*- coding:utf-8 -*-
from sqlalchemy import Column,Integer,Boolean,String,ForeignKey,desc,func
from sqlalchemy.orm import relationship

from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from flask import current_app
from app.models.base import Base
from app.models.base import db
from collections import namedtuple
__author__ = 'neo'
__time__ = '2018/9/12 11:00'




class Gift(Base):
    id = Column(Integer,primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    #数据库中并没有book，直接用接口返回的数据
    # book = relationship('Book')
    # bid = Column(Integer,ForeignKey('book.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean,default=False)

    def is_yourself_gift(self,uid):
        return True if self.uid == uid else False


    @classmethod
    def get_user_gifts(cls,uid):
        gifts = Gift.query.filter_by(uid=uid,launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls,isbn_list):
        count_list = db.session.query(func.count(Wish.id),Wish.isbn).filter(Wish.launched == False,Wish.isbn.in_(
            isbn_list),Wish.status==1).group_by(Wish.isbn).all()
        count_list = [{'count':w[0],'isbn':w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first


    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched = False).group_by(Gift.isbn).order_by(
            desc(Gift.create_time)).limit(current_app.config['REENET_BOOK_COUNT']).distinct().all()
        return recent_gift
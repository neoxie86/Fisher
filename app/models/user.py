# -*- coding:utf-8 -*-
from app.libs.helper import is_isbn_or_key
from app.models.base import db,Base
from sqlalchemy import Column,Integer,String,Boolean,Float
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager
from app.spider.yushu_book import YuShuBook
from app.models.gift import Gift
from app.models.wish import Wish


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

    def can_save_to_list(self,isbn):
        if is_isbn_or_key(isbn)!= 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 不允许一个用户同事赠送多本相同的图书
        # 一个用户不可能同事成为赠送者和索要者
        gifting = Gift.query.filter_by(uid=self.id,isbn=isbn,
                                       launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id,isbn=isbn,
                                       launched=False).first()
        # 既不在赠送清单，也不在心愿清单才能添加
        if not gifting and not wishing:
            return True
        else:
            return False
        
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
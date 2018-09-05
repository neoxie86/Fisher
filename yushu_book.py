# -*- coding:utf-8 -*-
__author__ = 'neo'
__time__ = '2018/9/5 16:48'

from httper import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls,keyword,count=15,start=0):
        url = cls.keyword_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result
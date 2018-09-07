# -*- coding:utf-8 -*-
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from flask import Flask, jsonify,request
from app.web import web
from app.forms.book import SearchForm
__author__ = 'neo'
__time__ = '2018/9/6 10:39'



@web.route('/book/search')
def search():
    """q:nomal,isbn
       page
       ?q=key&page=1

    """
    a=request
    q = request.args['q']
    page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
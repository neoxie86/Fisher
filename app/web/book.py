# -*- coding:utf-8 -*-
from flask import jsonify,request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.web import web
from app.view_models.book import BookCollection
import json

__author__ = 'neo'
__time__ = '2018/9/6 10:39'



@web.route('/book/search')
def search():
    """q:nomal,isbn
       page
       ?q=key&page=1
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.packge_single(result,q)
        else:
            yushu_book.search_by_keyword(q,page)
            # result = YuShuBook.search_by_keyword(q,page)
            # result = BookViewModel.packge_collection(result,q)
        books.fill(yushu_book,q)
        return json.dumps(books,default=lambda o:o.__dict__)
        # return jsonify(books.__dict__)
    else:
        return jsonify(form.errors)
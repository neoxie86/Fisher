# -*- coding:utf-8 -*-
__author__ = 'neo'
__time__ = '2018/9/5 11:12'

from flask import Flask
from helper import is_isbn_or_key
from yushu_book import YuShuBook
import json

app = Flask(__name__)
#载入配置文件
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q,page):
    """q:nomal,isbn
       page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return json.dumps(result),200,{'content-type':'application/json'}


# app.add_url_rule('/hello',view_func=hello)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])
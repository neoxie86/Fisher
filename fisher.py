# -*- coding:utf-8 -*-
__author__ = 'neo'
__time__ = '2018/9/5 11:12'
from app import create_app


app = create_app()

# app.add_url_rule('/hello',view_func=hello)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])
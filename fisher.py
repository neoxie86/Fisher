# -*- coding:utf-8 -*-
__author__ = 'neo'
__time__ = '2018/9/5 11:12'

from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return  'helloword'

# app.add_url_rule('/hello',view_func=hello)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
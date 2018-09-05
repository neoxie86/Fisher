# -*- coding:utf-8 -*-
__author__ = 'neo'
__time__ = '2018/9/5 15:37'

import requests

class HTTP(object):
    @staticmethod
    def get(url,return_json=True):
        r = requests.get(url)
        if r.status_code==200:
            if return_json:
                return r.json()
            else:
                return r.text
        else:
            if return_json:
                return {}
            else:
                return ''

# -*- coding:utf-8 -*-
from  wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired
__author__ = 'neo'
__time__ = '2018/9/6 17:31'

class SearchForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)
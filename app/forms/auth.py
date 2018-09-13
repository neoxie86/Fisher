# -*- coding:utf-8 -*-
from  wtforms import Form,StringField,IntegerField,PasswordField
from wtforms.validators import Length,NumberRange,DataRequired,Email,ValidationError
from app.models.user import User
__author__ = 'neo'
__time__ = '2018/9/12 14:44'

class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),
                                    Email(message='电子邮箱不符合规范')])
    password= PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'),
                                        Length(6,32)])
    nickname = StringField(validators=[DataRequired(),Length(2,10,message='昵称最少需要两个字符，最多十个字符')])

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('昵称已存在')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),
                                    Email(message='电子邮箱不符合规范')])
    password= PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'),
                                        Length(6,32)])
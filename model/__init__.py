# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 10:41
# @Author  : LY
# @FileName: __init__.py
# @Software: PyCharm
# @Official Accounts：大数据学习废话集

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255))
    keyword_id = db.Column(db.Integer)


class Keyword(db.Model):
    __tablename__ = 'keyword'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    keyword = db.Column(db.String(255))

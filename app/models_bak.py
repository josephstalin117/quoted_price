# -*- coding: utf-8 -*-
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, String, Table, Text, Time
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.types import YEAR
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Price(db.Model):
    """价格"""
    __tablename__ = 'price'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(255), doc='名称', default='Wanted User', nullable=False, unique=True)
    description = db.Column(db.String(128), doc='密码', nullable=False)
    payPassword = db.Column(db.String(32), doc='支付密码', nullable=False)
    money = db.Column(db.Float, doc='账户余额', default=50, nullable=False)
    description = db.Column(db.String(50), doc='个性签名', default='这个人很懒，什么也没留下', nullable=False)
    isAdmin = db.Column(db.Boolean, doc='是否管理员', default=False)

    orders = db.relationship('Order', backref='users', cascade='all', lazy='dynamic')
    coupons = db.relationship('Coupon', backref='users', cascade='all', lazy='dynamic')
    favorites = db.relationship('Favorite', backref='users', cascade='all', lazy='dynamic')
    comments = db.relationship('Comment', backref='users', cascade='all', lazy='dynamic')
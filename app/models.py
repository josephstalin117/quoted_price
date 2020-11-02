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
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.String(11))
    unit = db.Column(db.String(11))
    #unit = db.Column(db.String(11))
    #description = db.Column(db.String(50))
    #isAdmin = db.Column(db.Boolean, doc='是否管理员', default=False)
from flask import Flask, redirect
from flask import jsonify, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
from models import Price

import config
import os

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/show')
def show_price():
    #price_info1 = Price.query.filter_by(name = '实木课桌凳').first()
    price_info1 = Price.query.all()
    print("test")
    print(price_info1[0].name)
    return jsonify({'code': 1, 'msg': '请求成功', 'resData': "test"})

if __name__ == '__main__':
    app.run('0.0.0.0')
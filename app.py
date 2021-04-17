from flask import Flask, redirect
from flask import jsonify, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
from models import Price
from flask import render_template

import config
import os

# 创建Flask实例对象
app = Flask(__name__)
app.config.from_object(config)
# 获取SQLAlchemy实例对象，接下来就可以使用对象调用数据
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def show():
    item_name = request.args.get('item_name')
    #print(input_name)
    #items = Price.query.filter_by(name = '实木课桌凳').all()
    price_items = Price.query.filter_by(name = item_name).all()
    #print(price_items)
    return render_template('show.html', items=price_items)

if __name__ == '__main__':
    #启动服务，设置服务器地址和端口，0.0.0.0表示接收所有地址发来的请求
    #app.run('0.0.0.0')
    app.run(debug=True)
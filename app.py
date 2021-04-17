from flask import Flask, redirect
from flask import jsonify, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
from models import Price
from flask import render_template

import config
import os

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def show():
    item_name = request.args.get('item_name')
    #print(input_name)
    #items = Price.query.filter_by(name = '实木课桌凳').all()
    #print(items)
    price_items = Price.query.filter_by(name = item_name).all()
    #print(price_items)
    return render_template('show.html', items=price_items)

if __name__ == '__main__':
    app.run('0.0.0.0', port='5000', debug=True)
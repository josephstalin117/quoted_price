from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
import config
import os

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run('0.0.0.0')
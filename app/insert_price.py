import flask
import pandas
from .models import Price



if __name__ == '__main__':
    user_info1 = Price.query.filter_by(name = '实木课桌凳').first()
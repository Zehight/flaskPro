import sys
import config
import pymysql
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
app = Flask(__name__, instance_relative_config=True)


app.config['DEBUG'] = config.DEBUG
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/flask_demo'.format(config.username, config.password,
                                                                             config.db_address)

pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)

app.config.from_object('config')



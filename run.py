import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from gunicorn.app.base import BaseApplication
from application import GATEWAY

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(GATEWAY)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/flask_demo'.format(config.username, config.password,config.db_address)

pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)

app.config.from_object('config')


@app.route('/' + config.API_GATEWAY + '/health/check', methods=['GET'])
def check():
    return 'successful'


class GunicornApp(BaseApplication):
    def __init__(self, app):
        self.options = {
            'bind': '0.0.0.0:9000'
        }
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key, value)

    def load(self):
        return self.application


if __name__ == '__main__':
    gunicorn_app = GunicornApp(app)
    gunicorn_app.run()
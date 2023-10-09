from flask import Flask,Blueprint
import config

app = Flask(__name__, instance_relative_config=True)

API_GATEWAY = Blueprint(config.API_GATEWAY, __name__, url_prefix='/'+config.API_GATEWAY)


# 注册蓝图
from app.activity import activity
from app.user import user
from app.dept import dept
from app.file import file

API_GATEWAY.register_blueprint(activity)
API_GATEWAY.register_blueprint(user)
API_GATEWAY.register_blueprint(dept)
API_GATEWAY.register_blueprint(file)

app.register_blueprint(API_GATEWAY)


@app.route('/'+config.API_GATEWAY+'/health/check', methods=['GET'])
def check():
    return 'successful'

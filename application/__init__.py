from run import app
import config
from flask import Blueprint

API_GATEWAY_CONFIG = config.API_GATEWAY

API_GATEWAY = Blueprint(API_GATEWAY_CONFIG, __name__, url_prefix='/' + API_GATEWAY_CONFIG)

# 注册蓝图
from application.activity import activity
from application.user import user
from application.dept import dept
from application.file import file

API_GATEWAY.register_blueprint(activity)
API_GATEWAY.register_blueprint(user)
API_GATEWAY.register_blueprint(dept)
API_GATEWAY.register_blueprint(file)

app.register_blueprint(API_GATEWAY)


@app.route('/' + API_GATEWAY_CONFIG + '/health/check', methods=['GET'])
def check():
    return 'successful'
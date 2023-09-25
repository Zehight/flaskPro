from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# 注册蓝图
from app.wxcloudrun import demo

app.register_blueprint(demo)

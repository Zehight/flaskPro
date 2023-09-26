from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# 注册蓝图
from app.activity import activity
from app.user import user

app.register_blueprint(activity)
app.register_blueprint(user)

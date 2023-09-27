from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# 注册蓝图
from app.activity import activity
from app.user import user
from app.dept import dept

app.register_blueprint(activity)
app.register_blueprint(user)
app.register_blueprint(dept)

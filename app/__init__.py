from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# 注册蓝图
from app.activity import activity
from app.user import user
from app.dept import dept
from app.file import file

app.register_blueprint(activity)
app.register_blueprint(user)
app.register_blueprint(dept)
app.register_blueprint(file)


@app.route('/health/check', methods=['GET'])
def check():
    return 'successful'

from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')

# 加载控制器
from app.user import router



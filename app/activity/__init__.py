from flask import Blueprint

activity = Blueprint('activity', __name__, url_prefix='/activity')

# 加载控制器
from app.user import router



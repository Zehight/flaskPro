from flask import Blueprint

focus = Blueprint('focus', __name__, url_prefix='/focus')

# 加载控制器
from application.focus import router



from flask import Blueprint

focus = Blueprint('focus', __name__, url_prefix='/focus')

# 加载控制器
from app.focus import router



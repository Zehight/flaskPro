from flask import Blueprint

reply = Blueprint('reply', __name__, url_prefix='/reply')

# 加载控制器
from app.reply import router



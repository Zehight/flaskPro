from flask import Blueprint

relation = Blueprint('relation', __name__, url_prefix='/relation')

# 加载控制器
from app.relation import router



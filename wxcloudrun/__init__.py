from flask import Blueprint, request, jsonify

demo = Blueprint('demo', __name__, url_prefix='/demo')

# 加载控制器
from wxcloudrun import views



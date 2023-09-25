from flask import render_template, request
from app.activity import activity
from app.activity.response import make_succ_empty_response, make_succ_response, make_err_response


@activity.route('/getInfo', methods=['POST'])
def getInfo():
    #获取请求体
    params = request.get_json()
    #检验参数
    if 'key' not in params:
        return make_err_response('缺少action参数')


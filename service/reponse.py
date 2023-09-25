import json

from flask import Response

# 成功_空
def make_succ_empty_response():
    data = json.dumps({'code': 0, 'data': {},'msg':'empty'})
    return Response(data, mimetype='application/json')

# 成功_返回信息
def make_succ_response(data):
    data = json.dumps({'code': 0, 'data': data,'msg':'success'})
    return Response(data, mimetype='application/json')

# 失败_返回信息
def make_err_response(err_msg):
    data = json.dumps({'code': -1, 'msg': err_msg,'data':{}})
    return Response(data, mimetype='application/json')

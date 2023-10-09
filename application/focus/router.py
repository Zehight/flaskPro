import json

from flask import request
import application.focus.function as FocusFuncs
from application.focus import focus
import service.reponse as MyResponse
from service.login import token_required

# 点赞/收藏
@focus.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    msg, data = FocusFuncs.create_func(create_by=create_by,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@focus.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = FocusFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@focus.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = FocusFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@focus.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = FocusFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@focus.route('/list', methods=['POST'])
@token_required
def list():
    print(request.token_info)
    requestData = json.loads(request.data)
    msg, data = FocusFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)

import json

from flask import request
import application.reply.function as ReplyFuncs
from application.reply import reply
import service.reponse as MyResponse
from service.login import token_required


@reply.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    msg, data = ReplyFuncs.create_func(create_by=create_by,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@reply.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = ReplyFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@reply.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = ReplyFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@reply.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = ReplyFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@reply.route('/list', methods=['POST'])
@token_required
def list():
    print(request.token_info)
    requestData = json.loads(request.data)
    msg, data = ReplyFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)

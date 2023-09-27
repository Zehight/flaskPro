import json

from flask import request
import app.activity.function as ActivityFuncs
from app.activity import activity
import service.reponse as MyResponse
from service.login import token_required


@activity.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    dept_name = request.token_info['dept_name']
    create_by = request.token_info['id']
    msg, data = ActivityFuncs.create_func(create_by=create_by,dept_name=dept_name,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@activity.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = ActivityFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@activity.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = ActivityFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@activity.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = ActivityFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@activity.route('/list', methods=['POST'])
@token_required
def list():
    print(request.token_info)
    requestData = json.loads(request.data)
    msg, data = ActivityFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)

import json

from flask import request
import app.dept.function as DeptFuncs
from app.dept import dept
import service.reponse as MyResponse
from service.login import token_required


@dept.route('/add',methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    msg,data = DeptFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@dept.route('/update',methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg,data = DeptFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@dept.route('/delete',methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg,data = DeptFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@dept.route('/info',methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg,data = DeptFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@dept.route('/list',methods=['POST'])
def list():
    requestData = json.loads(request.data)
    msg,data = DeptFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

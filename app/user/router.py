import json

from flask import request
import app.user.function as UserFuncs
from app.user import user
import service.reponse as MyResponse

@user.route('/add',methods=['POST'])
def add():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/update',methods=['POST'])
def update():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/delete',methods=['POST'])
def delete():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/info',methods=['POST'])
def info():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@user.route('/list',methods=['POST'])
def list():
    requestData = json.loads(request.data)
    msg,data = UserFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

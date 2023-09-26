import json

from flask import request
import app.activity.function as ActivityFuncs
from app.activity import activity
import service.reponse as MyResponse

@activity.route('/add',methods=['POST'])
def add():
    requestData = json.loads(request.data)
    msg,data = ActivityFuncs.create_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@activity.route('/update',methods=['POST'])
def update():
    requestData = json.loads(request.data)
    msg,data = ActivityFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@activity.route('/delete',methods=['POST'])
def delete():
    requestData = json.loads(request.data)
    msg,data = ActivityFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

@activity.route('/info',methods=['POST'])
def info():
    requestData = json.loads(request.data)
    msg,data = ActivityFuncs.getinfo_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg,data = data)

@activity.route('/list',methods=['POST'])
def list():
    requestData = json.loads(request.data)
    msg,data = ActivityFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg,data = data)

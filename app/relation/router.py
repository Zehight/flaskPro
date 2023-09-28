import json

from flask import request
import app.relation.function as RelationFuncs
from app.relation import relation
import service.reponse as MyResponse
from service.login import token_required


@relation.route('/add', methods=['POST'])
@token_required
def add():
    requestData = json.loads(request.data)
    create_by = request.token_info['id']
    msg, data = RelationFuncs.create_func(create_by=create_by,**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@relation.route('/update', methods=['POST'])
@token_required
def update():
    requestData = json.loads(request.data)
    msg, data = RelationFuncs.update_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@relation.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = RelationFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@relation.route('/info', methods=['POST'])
@token_required
def info():
    requestData = json.loads(request.data)
    msg, data = RelationFuncs.getinfo_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)



@relation.route('/list', methods=['POST'])
@token_required
def list():
    print(request.token_info)
    requestData = json.loads(request.data)
    msg, data = RelationFuncs.getlist_func(**requestData)
    print(msg,data)
    return MyResponse.make_succ_response(msg=msg, data=data)

import json
import os
from flask import request, send_from_directory, current_app
import app.file.function as FileFuncs
from app.file import file
import service.reponse as MyResponse
from service.login import token_required


@file.route('/add', methods=['POST'])
@token_required
def add():
    file = request.files['file']
    requestData = request.form.to_dict()
    create_by = request.token_info['id']
    msg, data = FileFuncs.create_func(real_file=file, create_by=create_by, **requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@file.route('/delete', methods=['POST'])
@token_required
def delete():
    requestData = json.loads(request.data)
    msg, data = FileFuncs.delete_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@file.route('/list', methods=['POST'])
@token_required
def list():
    requestData = json.loads(request.data)
    msg, data = FileFuncs.getlist_func(**requestData)
    return MyResponse.make_succ_response(msg=msg, data=data)


@file.route('/preview', methods=['GET'])
def preview():
    id = request.args.get('id')
    msg, data = FileFuncs.getinfo_func(id=id)
    fileName = data['file_name']
    return send_from_directory(os.path.join(os.path.dirname(current_app.root_path), 'files'), id + '_' + fileName)

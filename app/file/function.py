from sqlalchemy.exc import IntegrityError
import os
from service.login import token_required
from service.models import File
from PIL import Image

file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../files'))
# 新增
def create_func(real_file,**kwargs):
    print(real_file)
    file_name = real_file.filename
    file = File.create(file_name=file_name, **kwargs)
    file_path=os.path.join(file_folder, file.id+'_'+file_name)
    real_file.save(file_path)

    small_file = File.create(file_name=file_name,small_type='1', **kwargs)
    file.update(small_id = small_file.id)
    small_file_path = os.path.join(file_folder, small_file.id+'_'+file_name)
    with Image.open(file_path) as small_real_file:
        small_real_file.save(small_file_path, optimize=True, quality=20)
    return "操作成功",'文件上传成功'

# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    file = File.get(id=kwargs['id'])
    if file:
        file.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    file = File.get(id=kwargs['id'])
    if file:
        return "操作成功",file.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = File.search(**kwargs)
    return "操作成功",result

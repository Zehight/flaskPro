import os
import sys
from io import BytesIO
from flask import current_app
from service.models import File
from PIL import Image
import config


from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


cos_config = CosConfig(Region='ap-shanghai', SecretId=config.SecretId, SecretKey=config.SecretKey, Token=None)
client = CosS3Client(cos_config)

response = client.list_buckets()
print(response)






# 新增
def create_func(real_file, **kwargs):
    file_name = real_file.filename
    file = File.create(file_name=file_name, **kwargs)
    file_save_name = file.id + '_' + file_name
    client.put_object(
        Bucket='img-1259115987',
        Body=real_file.read(),
        Key=file_save_name,
        EnableMD5=False
    )

    small_file = File.create(file_name=file_name, small_type='1', **kwargs)
    file.update(small_id=small_file.id)
    small_file_save_name = small_file.id + '_' + file_name
    with Image.open(real_file) as small_real_file:
        small_real_file.save(small_file_save_name, optimize=True, quality=20)
        client.put_object_from_local_file(
            Bucket='small-img-1259115987',
            LocalFilePath=small_file_save_name,
            Key=small_file_save_name
        )
        os.remove(small_file_save_name)
    return "操作成功", '文件上传成功'


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '数据信息错误'
    file = File.get(id=kwargs['id'])
    if file:
        file.delete()
        return "操作成功", '数据删除成功'
    else:
        return "操作失败", '数据不存在'


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '参数错误'
    file = File.get(id=kwargs['id'])
    if file:
        return "操作成功", file.to_dict()
    else:
        return "操作失败", '数据不存在'


# 分页查询列表
def getlist_func(**kwargs):
    result = File.search(**kwargs)
    return "操作成功", result

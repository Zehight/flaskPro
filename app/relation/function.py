from sqlalchemy.exc import IntegrityError

from service.login import token_required
from service.models import Relation


# 新增
def create_func(**kwargs):
    try:
        relation = Relation.create(**kwargs)
        print(relation.to_dict())
        return "操作成功",relation.id
    except IntegrityError as e:
        print(e)
        if 'Duplicate entry' in str(e):
            return "操作失败","数据信息重复"
        else:
            return "操作失败","服务器错误"


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    relation = Relation.get(id=kwargs['id'])
    if relation:
        relation.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    relation = Relation.get(id=kwargs['id'])
    if relation:
        try:
            relation.update(**kwargs)
            return "操作成功","数据修改成功"
        except IntegrityError as e:
            print(e)
            if 'Duplicate entry' in str(e):
                return "操作失败","数据信息重复"
            else:
                return "操作失败","服务器错误"
    else:
        return "操作失败",'数据不存在'


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'参数错误'
    relation = Relation.get(id=kwargs['id'])
    if relation:
        return "操作成功",relation.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Relation.search(**kwargs)
    return "操作成功",result

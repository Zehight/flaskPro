from sqlalchemy.exc import IntegrityError

from service.login import token_required
from service.models import Reply


# 新增
def create_func(**kwargs):
    try:
        reply = Reply.create(**kwargs)
        print(reply.to_dict())
        return "操作成功",reply.id
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
    reply = Reply.get(id=kwargs['id'])
    if reply:
        reply.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    reply = Reply.get(id=kwargs['id'])
    if reply:
        try:
            reply.update(**kwargs)
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
    reply = Reply.get(id=kwargs['id'])
    if reply:
        return "操作成功",reply.to_dict()
    else:
        return "操作失败",'数据不存在'

# 分页查询列表
def getlist_func(**kwargs):
    result = Reply.search(**kwargs)
    return "操作成功",result

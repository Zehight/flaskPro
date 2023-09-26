from sqlalchemy.exc import IntegrityError

from service.models import User


# 新增
def create_func(**kwargs):
    try:
        user = User.create(**kwargs)
        return "操作成功",user.id
    except IntegrityError as e:
        if 'Duplicate entry' in str(e):
            return "操作失败","数据信息重复"
        else:
            return "操作失败","服务器错误"


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败",'数据信息错误'
    user = User.get(id=kwargs['id'])
    if user:
        user.delete()
        return "操作成功",'数据删除成功'
    else:
        return "操作失败",'数据不存在'


# 更新
def update_func(**kwargs):
    user = User.get(id=kwargs['id'])
    print(user.to_dict())
    if user:
        try:
            user.update(**kwargs)
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
    user = User.get(id=kwargs['id'])
    if user:
        return "操作成功",user.to_dict()
    else:
        return "操作失败",'数据不存在'


# 分页查询列表
def getlist_func(pageDto=None, keyword=''):
    if pageDto == None:
        return 'error'
    page = pageDto['page']
    rows = pageDto['rows']
    result = User.search(keyword, page=page, rows=rows)
    return "操作成功",result

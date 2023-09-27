from datetime import datetime, timedelta

from sqlalchemy.exc import IntegrityError
from service.models import User,Dept

import jwt
import bcrypt

SECRET_KEY = '12dwafdsgefdsvdfgrteweddsfthrefsdvfbtrhrerdsdvbthrefdvfbthedsdvfgredsfgrds3456'


# 新增
def create_func(**kwargs):
    try:
        kwargs['pwd'] = bcrypt.hashpw(kwargs['pwd'].encode(), bcrypt.gensalt())
        user = User.create(**kwargs)
        return "操作成功", user.id
    except IntegrityError as e:
        if 'Duplicate entry' in str(e):
            return "操作失败", "数据信息重复"
        else:
            return "操作失败", "服务器错误"


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '数据信息错误'
    user = User.get(id=kwargs['id'])
    if user:
        user.delete()
        return "操作成功", '数据删除成功'
    else:
        return "操作失败", '数据不存在'


# 更新
def update_func(**kwargs):
    user = User.get(id=kwargs['id'])
    print(user.to_dict())
    if user:
        try:
            user.update(**kwargs)
            return "操作成功", "数据修改成功"
        except IntegrityError as e:
            print(e)
            if 'Duplicate entry' in str(e):
                return "操作失败", "数据信息重复"
            else:
                return "操作失败", "服务器错误"
    else:
        return "操作失败", '数据不存在'


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '参数错误'
    user = User.get(id=kwargs['id'])
    if user:
        return "操作成功", user.to_dict()
    else:
        return "操作失败", '数据不存在'


# 分页查询列表
def getlist_func(**kwargs):
    result = User.search(**kwargs)
    return "操作成功", result


def generate_token(kwargs):
    # 设置过期时间为 1 小时后
    expire_time = datetime.utcnow() + timedelta(hours=1)
    dept = Dept.get(id=kwargs['dept_id'])
    kwargs['pwd']="嘿嘿🤭，你猜？"
    payload = {
        **kwargs,
        "dept_name": dept.to_dict()['name'],
        'exp': expire_time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def login_func(**kwargs):
    user = User.get(user_name=kwargs['user_name'])
    if user:
        if bcrypt.checkpw(kwargs['pwd'].encode(), user.pwd.encode()):
            token = generate_token(user.to_dict())
            return "操作成功",token
        else:
            return "操作失败", "错误的用户名或密码"
    else:
        return "操作失败", "错误的用户名或密码"

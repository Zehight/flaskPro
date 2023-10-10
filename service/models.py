import uuid
from datetime import datetime
from service.default_dao import CRUDMixin
from run import db

class Dept(db.Model,CRUDMixin):
    __tablename__ = 'dept'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    name = db.Column(db.String(50))
    cover_id = db.Column(db.String(50))

class User(db.Model, CRUDMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    dept_id = db.Column(db.String(50))
    user_name = db.Column(db.String(50), unique=True)
    nike_name = db.Column(db.String(50))
    pwd = db.Column(db.String(255))
    phone = db.Column(db.String(50), unique=True)
    search_fields = ['real_name','nike_name', 'phone']

class Activity(db.Model,CRUDMixin):
    __tablename__ = 'activity'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    status = db.Column(db.String(1), nullable=False,default="0") # 删除为1，不删除为0
    top = db.Column(db.String(1), nullable=True,default="0") # 置顶
    excellent = db.Column(db.String(1), nullable=True,default="0") # 加精
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(16000), nullable=False)
    dept_name = db.Column(db.String(50), nullable=False)
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    search_fields = ['title', 'content','create_by','dept_name']

class File(db.Model,CRUDMixin):
    __tablename__ = 'file'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    status = db.Column(db.String(1), nullable=False, default="0")  # 删除为1，不删除为0
    file_name = db.Column(db.String(100), nullable=False)
    use_type = db.Column(db.String(1), nullable=False, default="0") #0:活动中的图片 1：头像 2：测试
    small_type = db.Column(db.String(1), nullable=False, default="0") #0:原图  1：缩放后的图
    small_id = db.Column(db.String(50))
    activity_id = db.Column(db.String(50))
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    search_fields = ['file_name']

class Reply(db.Model,CRUDMixin):
    __tablename__ = 'reply'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    activity_id = db.Column(db.String(50))
    reply_id = db.Column(db.String(50))
    content = db.Column(db.String(600))
    status = db.Column(db.String(1), nullable=False, default="0")  # 删除为1，不删除为0
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    search_fields = ['content']

class Focus(db.Model,CRUDMixin):
    __tablename__ = 'focus'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    activity_id = db.Column(db.String(50))
    type = db.Column(db.String(1), nullable=True)  # 点赞为0，收藏为1
    status = db.Column(db.String(1), nullable=False, default="0")  # 不删除为0，删除为1
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class Relation(db.Model,CRUDMixin):
    __tablename__ = 'relation'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    main_id = db.Column(db.String(50)) # 关联着ID
    type = db.Column(db.String(1), nullable=True)  # 关注为0，被关注为1
    status = db.Column(db.String(1), nullable=False, default="0")  # 删除为1，不删除为0
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


db.create_all()

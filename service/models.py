import uuid
from datetime import datetime
from run import db
from service.default_dao import CRUDMixin

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
    father_field = 'dept_id'

class Activity(db.Model,CRUDMixin):
    __tablename__ = 'activity'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    status = db.Column(db.String(1), nullable=False,default="0") # 删除为1，不删除为0
    top = db.Column(db.String(1), nullable=True,default="0") # 置顶
    excellent = db.Column(db.String(1), nullable=True,default="0") # 加精
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(16000), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    dept_name = db.Column(db.String(50), nullable=False)
    create_by = db.Column(db.String(50), nullable=False)
    search_fields = ['title', 'content','create_by','dept_name']
    father_field = 'create_by'


db.create_all()

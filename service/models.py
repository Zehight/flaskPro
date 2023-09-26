from datetime import datetime

from run import db
from service.default_dao import CRUDMixin


class User(db.Model, CRUDMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    search_fields = ['name', 'email']

class Activity(db.Model,CRUDMixin):
    __tablename__ = 'activity'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(1), nullable=False,default="0") # 删除为1，不删除为0
    top = db.Column(db.String(1), nullable=True,default="0") # 置顶
    excellent = db.Column(db.String(1), nullable=True,default="0") # 加精
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(16000), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    create_by = db.Column(db.Integer, nullable=False)
    search_fields = ['title', 'content','create_by']


db.create_all()

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
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    BlogStatus = db.Column(db.String(1), nullable=False)
    Top = db.Column(db.String(1), nullable=True)
    Excellent = db.Column(db.String(1), nullable=True)
    TemplateId = db.Column(db.BigInteger, nullable=False)
    Theme = db.Column(db.String(100), nullable=False)
    Keyword = db.Column(db.String(10), nullable=True)
    Content = db.Column(db.String(20000), nullable=False)
    LikeNum = db.Column(db.BigInteger, nullable=True)
    ViewNum = db.Column(db.BigInteger, nullable=True)
    PublishDate = db.Column(db.Date, nullable=False, default=date.today())
    ModifyDate = db.Column(db.Date, nullable=False, default=date.today())


db.create_all()

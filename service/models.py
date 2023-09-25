from run import db
from service.default_dao import CRUDMixin


class User(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    search_fields = ['name', 'email']


db.create_all()

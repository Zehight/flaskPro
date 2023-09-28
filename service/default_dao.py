from run import db
from sqlalchemy import or_
from datetime import datetime

class CRUDMixin:
    def __init__(self):
        self.__mapper__ = None

    # def to_dict(self):
    #     def format_datetime(dt):
    #         return dt.strftime('%Y-%m-%d %H:%M:%S')
    #     return {
    #         prop: format_datetime(getattr(self, prop)) if isinstance(getattr(self, prop), datetime) else getattr(self,
    #                                                                                                              prop)
    #
    #         for prop in vars(self) if
    #         not prop.startswith('_') and not callable(getattr(self, prop)) and not isinstance(getattr(self, prop),
    #                                                                                           db.Model)}

    def to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            value = getattr(self, key)
            if isinstance(value, datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            result[key] = value
        return result

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()

    @classmethod
    def get(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def get_or_create(cls, defaults=None, **kwargs):
        instance = cls.get(**kwargs)
        if instance:
            return instance, False
        else:
            params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, db.Column))
            params.update(defaults or {})
            return cls.create(**params), True

    @classmethod
    def count(cls):
        return cls.query.count()

    @classmethod
    def filter(cls, *criterion):
        return cls.query.filter(*criterion)

    @classmethod
    def all(cls):
        return cls.query.all()

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    @classmethod
    def search(cls, keyword = '',page=1, rows=10,**kwargs):
        query = cls.query
        if hasattr(cls, 'search_fields') and keyword:
            query = query.filter(or_(*[getattr(cls, field).ilike(f'%{keyword}%') for field in cls.search_fields]))
        query = query.filter_by(**kwargs)
        total = query.count()
        pagination = query.paginate(page, rows, error_out=False)

        items = [item.to_dict() for item in pagination.items]
        return {
            'page': page,
            'rows': rows,
            'total': total,
            'list': items
        }
from service.models import User


def create_func():
    user = User.search(keyword='john')
    print(user)
    return user



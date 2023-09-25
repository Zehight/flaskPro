import app.user.function as UserFuncs
from app.user import user
import service.reponse as MyResponse

@user.route('/')
def index():
    data = UserFuncs.create_func()
    """
    :return: 返回index页面
    """
    return 'aa'
    # return MyResponse.make_succ_response(data)

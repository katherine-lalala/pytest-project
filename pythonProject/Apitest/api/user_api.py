from core.api_util import api_util
from utils.response_util import process_response


#
def send_code(json_data):
    """
    获取短信验证码
    :return:
    """
    response = api_util.get_code(json=json_data)
    return process_response(response)  #process_response是处理http请求的，看状态码是否是200/201


#注册

def register(code, mobile):
    # 注册接口
    json_data = {
        "code": str(code),
        "passwd": 123456,
        "username": str(mobile)
    }
    response = api_util.register_mobile(json=json_data)
    return process_response(response)


def login(username, password):
    """
    用户登陆接口
    :param username:
    :param password:
    :return:
    """
    json_data = {
        "username": username,
        "password": password
    }
    response = api_util.user_login(json=json_data)
    return process_response(response)


def add_shopping_cart(params, token):
    """
    添加购物车
    :param token:
    :param params:
    :return:
    """

    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.add_shopping(json=params, headers=headers)
    return process_response(response)
#  返回状态码是否是200

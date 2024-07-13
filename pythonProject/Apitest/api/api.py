import requests
from core.api_util import api_util
from utils.response_util import process_response


def mobile_query(param):

 #把方法用get封装起来，直接引用get方法并传入参数即可，而无需每次写requests.get

    response = api_util.get_mobile_belong(params=param)  #params是行参，param是实参
    result = process_response(response)
    return result


def json_method(json_data):
    """
    这个方法测试json传参
    :param json_data:
    :return:
    """
    response = api_util.post_data(json=json_data)
    process_response(response)
    return response.json()



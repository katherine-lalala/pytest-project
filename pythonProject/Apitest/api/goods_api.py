from core.api_util import api_util
from utils.response_util import process_response


def get_banner():
    """
    获取banner接口
    :return:
    """
    response = api_util.banner()
    #banner方法是获取完整的“banner”接口链接(http://admin.5istudy.online/banners/)
    return process_response(response)
    #process_response方法是根据上面获得的response去请求结果，并返回是否200


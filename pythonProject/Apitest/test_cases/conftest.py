from utils.read import base_data
import pytest, os
from api.user_api import login


def get_data():
    return base_data.read_data()


@pytest.fixture()
def login_fixture():
    if 'token' not in os.environ:
        data = get_data()['login_fixture']
        mobile = data['mobile']
        password = data['password']
        ##登录接口
        result = login(mobile, password)
        os.environ['token'] = result.body['token']
        os.environ['mobile'] = str(mobile)
        return result.body['token'], mobile
    else:
        return os.environ['token'], os.environ['mobile']

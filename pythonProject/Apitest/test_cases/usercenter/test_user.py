import allure
import pytest

from core.api_util import api_util
from test_cases.conftest import get_data
from test_cases.usercenter.conftest import get_code
from utils.read import base_data
from api.user_api import send_code, register, login, add_shopping_cart


@allure.feature("用户中心模块")
class TestUser:
    @allure.story("用户注册后登陆")
    @allure.title("注册手机号测试用例")
    def test_register(self):
        json_data = base_data.read_data()['test_register']
        # # 发送短信验证码
        result = send_code(json_data)
        assert result.success is True
        # 获取短信验证码
        mobile = result.body['mobile']
        code = get_code(mobile)
        # 注册
        register_result = register(code, mobile)
        assert register_result.success is True

    @pytest.mark.parametrize('username, password', get_data()['user_login'])
    @allure.story("用户登录")
    @allure.title("用户手机号登录")
    def test_login(self, username, password):
        print(username, password)
        result = login(username, password)
        assert result.success is True
        assert result.body['token'] is not None

    @allure.story("购物车相关")
    @allure.title("加购物车")
    @pytest.mark.parametrize('username, password', get_data()['user_login'])
    def test_shopping_cart(self, username, password):
        #登陆接口
        result = login(username, password)
        token = result.body['token']
        param = get_data()["shopping_cart"]
        result = add_shopping_cart(param, token)
        #查询购物车数量
        get_shop_cart_num(username, param['goods'])
        assert result.success is True

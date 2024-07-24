import allure
import pytest

from core.api_util import api_util
from test_cases.conftest import get_data
from test_cases.usercenter.conftest import get_code, get_shop_cart_num, delete_user
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
        ## 注册
        register_result = register(code, mobile)
        assert register_result.success is True
        #删除用户
        # delete_user(mobile)


    @pytest.mark.parametrize('username, password', get_data()['user_login'])
    @allure.story("用户登录")
    @allure.title("用户手机号登录")
    def test_login(self, username, password):
        # print(username, password)
        result = login(username, password)
        assert result.success is True
        assert result.body['token'] is not None

    @allure.story("购物车相关")
    @allure.title("加购物车")
    def test_shopping_cart(self, login_fixture):
        token = login_fixture[0]
        username = login_fixture[1]
        param = get_data()["shopping_cart"]
        result = add_shopping_cart(param, token)
        assert result.success is True
        #查询购物车数量
        num = get_shop_cart_num(username, param['goods'])
        assert result.body['nums'] == num #验证接口返回数据等于数据库的数量

    @allure.story("购物车相关")
    @allure.title("加购物车")
    def test_shopping_cart2(self, login_fixture):
        token = login_fixture[0]
        username = login_fixture[1]
        param = get_data()["shopping_cart"]
        result = add_shopping_cart(param, token)
        assert result.success is True
        #查询购物车数量
        num = get_shop_cart_num(username, param['goods'])
        assert result.body['nums'] == num #验证接口返回数据等于数据库的数量


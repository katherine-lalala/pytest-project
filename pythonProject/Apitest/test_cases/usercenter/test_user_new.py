import allure
import pytest

from core.ApiService import ApiService
from utils.YamlUtil import YamlUtils


@allure.feature("用户中心模块")
class TestUser:
    @pytest.mark.parametrize("data", YamlUtils().read_testcases_yaml('user_center.yaml', 'user_login_new'))
    def test_user_new(self, data):
        print(data)

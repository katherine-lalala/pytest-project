import allure

from api.goods_api import get_banner
from test_cases.goodscenter.conftest import banner_num


@allure.feature("用户中心模块")
class TestGoods:
    @allure.story("首页展示内容")
    @allure.title("banner")
    def test_banner(self):
        num = banner_num()
        result = get_banner()
        assert result.success is True
        assert len(result.body) == num

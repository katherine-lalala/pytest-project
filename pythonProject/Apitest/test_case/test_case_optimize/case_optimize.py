import requests
import pytest
from api.api import mobile_query
from utils.read import base_data

url = base_data.read_ini()['host']['api_url']


def test_mobile():
    param = base_data.read_data()["mobile_belong"]
    # print(param)
    result = mobile_query(param)
    assert result.success is True
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "北京"
    assert result['result']["city"] == "北京"
    assert result['result']["company"] == "中国移动"
    # assert result['result']["cardtype"] is None
    assert result['result']["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()

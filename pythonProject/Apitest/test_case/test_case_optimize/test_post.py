import requests
import pytest
from api.api import json_method
from utils.log_util import logger
from utils.read import base_data



def test_post():
    logger.info("开始执行test_post方法")
    json_data = base_data.read_data()["json_data"]
    result = json_method(json_data)
    assert result['id'] == 101
    logger.info("用例执行完毕")


if __name__ == '__main__':
    pytest.main()

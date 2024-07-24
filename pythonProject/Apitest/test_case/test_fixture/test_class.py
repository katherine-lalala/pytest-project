import requests
import pytest


@pytest.fixture(scope="class")
def func():
    print("我是前置步骤")


class TestClassFixture:
    def test_mobile(self):

        print("测试手机归属地get请求")
        params = {'key1': 'value1', 'key2': 'value2'}
        r = requests.get("https://httpbin.org/get", params=params)
        print(r.status_code)
        assert r.status_code == 200
        res = r.json()
        assert res['url'] == 'https://httpbin.org/get?key1=value1&key2=value2'
        assert res['origin'] == '39.148.79.222'
        assert res['args']['key1'] == 'value1'
        assert res['args']['key2'] == 'value2'

    def test_mobile_post(self, func):
        print("测试post请求")
        params = {'key': 'value'}
        r = requests.post('https://httpbin.org/post', data=params)
        print(r.status_code)
        assert r.status_code == 200
        print(r.json())
        res = r.json()
        assert res['args'] == {}
        assert res['data'] == ''
        assert res['form']['key'] == 'value'


if __name__ == '__main__':
    pytest.main()

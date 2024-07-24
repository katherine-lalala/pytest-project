import json

import requests

from utils.log_util import logger
from utils.read import base_data

api_root_url = base_data.read_ini()['host']['api_url']


class RestClient:
    def __init__(self):
        self.api_root_url = api_root_url
        self.session = requests.Session()



    def get(self, url, **kwargs):
        return requests.get(self.api_root_url + url, **kwargs)

    def post(self, url, **kwargs):
        return requests.post(self.api_root_url + url, **kwargs)

    def put(self, url, **kwargs):
        return requests.put(self.api_root_url + url, **kwargs)

    def delete(self, url, **kwargs):
        return requests.delete(self.api_root_url + url, **kwargs)

    def request(self, method, url, **kwargs):
        self.request_log(url, method, **kwargs)
        if method == 'GET':
            return self.session.get(self.api_root_url + url, **kwargs)
        if method == 'POST':
            return self.session.post(self.api_root_url + url, **kwargs)
        if method == 'PUT':
            return self.session.put(self.api_root_url + url, **kwargs)
        if method == 'DELETE':
            return self.session.delete(self.api_root_url + url, **kwargs)

        def request_log(self, url, method, **kwargs):
            data = dict(**kwargs).get("data")
            json_data = dict(**kwargs).get("json")
            params = dict(**kwargs).get("params")
            headers = dict(**kwargs).get("headers")

            logger.info("接口请求的地址>>>\n{}".format(self.api_root_url + url))
            logger.info("接口请求的方法>>>\n{}".format(method))
            if data is not None:
                logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, ensure_ascii=False, indent=2)))
            if json_data is not None:
                logger.info("接口请求的json参数>>>\n{}".format(json.dumps(json_data, ensure_ascii=False, indent=2)))
            if params is not None:
                logger.info("接口请求的params参数>>>\n{}".format(json.dumps(params, ensure_ascii=False)))
            if headers is not None:
                logger.info("接口请求的json参数>>>\n{}".format(json.dumps(headers, ensure_ascii=False, indent=2)))


Api = RestClient()

from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_mobile_belong(self, **kwargs):
        return self.get('/shouji/query', **kwargs)

    def post_data(self, **kwargs):
        return self.post("/posts", **kwargs)

    # 以下是项目实战的方法
    def get_code(self, **kwargs):
        return self.post("/code/", **kwargs)  #此处是用requests.post方法，发送请求

    def register_mobile(self, **kwargs):
        return self.post("/users/", **kwargs)

    def user_login(self, **kwargs):
        return self.post("/login/", **kwargs)

    # goods_api
    def banner(self, **kwargs):
        return self.get("/banners/", **kwargs)

    def add_shopping(self, **kwargs):
        return self.post("/shopcarts/", **kwargs)


api_util = Api()  #Api类的初始化

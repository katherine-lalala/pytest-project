import requests
req = requests.session()

url = "http://sellshop.5istudy.online/sell/user/login_page"
data = {
    "username": "test01",
    "password": "123456"
}
res = req.post(url, data=data)
print(res.text)
url2 = "http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10"
res2 = req.get(url2)


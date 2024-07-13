import requests

def test_mobile():
    r = requests.get(url="http://api.binstd.com/shouji/query", params={
        "shouji": "13456755448",
        "appkey": "0c818521d38759e1"
    })
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()

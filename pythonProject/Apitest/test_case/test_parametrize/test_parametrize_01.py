import pytest

# @pytest.mark.parametrize("name", ["老马"])
# def test_parametrize(name):
#     print("测试paramatrize")
#     print("我是" + name)

#单参数多次循环
@pytest.mark.parametrize("name",["安其拉","黄忠","大乔"])
def test_parametrize(name):
    assert name == "安其拉"


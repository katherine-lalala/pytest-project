import pytest


@pytest.fixture(scope="session")
def test_session():
    print("我是session级别的fixture")


@pytest.fixture(scope="function")
def test_func1():
    print("我是func级别的fixture")


@pytest.fixture(scope="function", autouse=True)
def func():
    print("yield before")
    yield "老白"
    print("yield after")

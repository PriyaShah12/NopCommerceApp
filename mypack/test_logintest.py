import pytest
@pytest.fixture()
def setup():
    print("Once before every method")
    yield
    print("Once After every method")

def test_LoginFb(setup):
    print("Login By Fb")

def test_loginByTwitter(setup):
    print("Login By Twitter")
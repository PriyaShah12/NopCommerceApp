import pytest
@pytest.fixture()
def setup():
    print("Once before every method")
    yield
    print("Once After every method")

def test_signInFb(setup):
    print("SignIn By Fb")

def test_SignInByTwitter(setup):
    print("SignIn By Twitter")
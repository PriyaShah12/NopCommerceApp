from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

#s=Service("C:\Python_durgasir\lib/chromedriver.exe")
@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        s = Service("C:\Python_durgasir\lib/chromedriver.exe")
        driver=webdriver.Chrome(service=s)
    elif browser =='Firefox':
        driver=webdriver.Firefox()
    else:
        s = Service("C:\Python_durgasir\lib/chromedriver.exe")
        driver=webdriver.Chrome(service=s)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

#************HTMLreport*********************

def pytest_configure(config):
    config._metadata["Project Name"] = "NOP Commerce"
    config._metadata["Tester"] = "Priya"


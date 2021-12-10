from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.driver import OperaDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser =='Firefox':
        s = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    elif browser=="Edge":
        s=Service(EdgeChromiumDriverManager().install())
        driver= webdriver.Ie(service=s)
    elif browser == "Opera":
        s= Service(executable_path=OperaDriver().install())
        driver= webdriver.Opera(service_args=s)
    else:
        s = Service(IEDriverManager().install())
        driver = webdriver.Chrome(service=s)
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

@pytest.mark.optionalhook
def pytest_configure(config):
    config._metadata.pop("JAVA_HOME",None)
    config._metadata.pop("Plugins", None)


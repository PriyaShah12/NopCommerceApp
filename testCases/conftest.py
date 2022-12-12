from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        print("############################")
        s= Service(executable_path="C:\\Priya_Dev\\chromedriver\\chromedriver.exe")
        # s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser =='Firefox':
        s = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    elif browser=="Edge":
        s=Service(EdgeChromiumDriverManager().install())
        driver= webdriver.Ie(service=s)

    else:
        s = Service(IEDriverManager().install())
        driver = webdriver.Chrome(service=s)
    return driver

def pytest_addoption(parser):  #This will get value from CLI/hook
    parser.addoption("--browser")


@pytest.fixture
def browser(request):  #This will return browser value to setup method
    return request.config.getoption("--browser")

#************HTMLreport*********************

#it is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "NOP Commerce"
    config._metadata["Tester"] = "Priya"


#This hook is for delete/modify Environment info to the HTML Report
# @pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)


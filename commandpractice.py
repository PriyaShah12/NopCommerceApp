
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.firefox import GeckoDriverManager

s=Service(executable_path=GeckoDriverManager().install())
driver=webdriver.Firefox(service=s)
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("ABC")

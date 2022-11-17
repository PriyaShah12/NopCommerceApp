from selenium import webdriver
import pytest
from pageObject.LoginPage import Login
from utilities.readproperties import configRead
from utilities.customLogger import LogGen

class Test_001_login:
    base_url=configRead.ReadUrl()
    username=configRead.ReadUsername()
    password=configRead.Readpassword()
    logger= LogGen.loggen()

    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.logger.info("*******************Test_001_login******************************")
        self.logger.info("*****************verifying home page title *************************")
        self.driver=setup
        self.driver.get(self.base_url)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************Home page Test case passed***********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            self.driver.close()
            self.logger.error("****************Home Page test case failed**************************")

            assert False
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***************Test login started*******************")
        self.driver=setup
        self.driver.get(self.base_url)
        self.lp= Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*************Test login passed***************")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")

            self.logger.info("****************Test Login failed***********************")
            assert False
        self.driver.close()


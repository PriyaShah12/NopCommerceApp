from selenium import webdriver
import pytest
from pageObject.LoginPage import Login
from utilities.readproperties import configRead
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_001_login:
    base_url=configRead.ReadUrl()
    path=".//TestData/DDT_testsheet.xlsx"
    logger= LogGen.loggen()
    @pytest.mark.regression
    def test_homepagetitle_ddt(self,setup):
        self.logger.info("*******************Test_ddt_001_login******************************")
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

    def test_login_ddt(self,setup):
        self.logger.info("***************Test login_DDT started*******************")
        self.driver=setup
        self.driver.get(self.base_url)
        self.lp= Login(self.driver)
        self.rows=XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of rows:", self.rows)
        report=[]
        for r in range(2, self.rows+1):
            self.usrname = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.pswd = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.usrname)
            self.lp.setPassword(self.pswd)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration123"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("Test case passed")

                    self.lp.clickLogout()
                    report.append('pass')
                elif self.exp == "fail":
                    self.logger.info("Test case failed")
                    self.lp.clickLogout()
                    report.append('fail')
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("Test case failed")
                    report.append('fail')
                elif self.exp == 'fail':
                    self.logger.info("Test case passed")
                    report.append('pass')

            if 'fail' not in report:
                self.logger.info("DDT Case passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("DDT Failed")
                self.driver.close()
                assert False
        self.logger.info("*****************End of DDT****************** ")

















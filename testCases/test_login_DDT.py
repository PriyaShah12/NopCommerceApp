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
    # @pytest.mark.regression
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

    @pytest.mark.skip(reason="Run Later")
    def test_login_ddt(self,setup):
        self.logger.info("***************Test login_DDT started*******************")
        self.driver=setup
        self.driver.get(self.base_url)
        self.lp= Login(self.driver)
        time.sleep(5)
        self.rows=XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of rows:", self.rows)
        report=[]
        time.sleep(3)
        for r in range(2, self.rows+1):
            self.usrname = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.pswd = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            time.sleep(3)
            self.lp.setUserName(self.usrname)
            self.lp.setPassword(self.pswd)
            self.lp.clickLogin()
            time.sleep(3)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("Test case passed")

                    self.lp.clickLogout()
                    time.sleep(3)
                    report.append('pass')
                elif self.exp == "fail":
                    self.logger.info("Test case failed")
                    self.lp.clickLogout()
                    time.sleep(3)
                    report.append('fail')
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("Test case failed")
                    report.append('fail')
                    time.sleep(3)
                elif self.exp == 'fail':
                    self.logger.info("Test case passed")
                    report.append('pass')
                    time.sleep(3)

            if 'fail' not in report:
                self.logger.info("DDT Case passed")
                self.driver.close()
                time.sleep(3)
                assert True
            else:
                self.logger.info("DDT Failed")
                self.driver.close()
                time.sleep(3)
                assert False
        self.logger.info("*****************End of DDT****************** ")

















from pageObject.LoginPage import Login
from pageObject.AddCustomer import AddCustomer
from utilities.customLogger import LogGen
from utilities.readproperties import configRead
from pageObject.searchcustomerpage import searchcustomer
import pytest
import time

class Test_SearchCustomerByEmail_004:
    username=configRead.ReadUsername()
    password=configRead.Readpassword()
    url=configRead.ReadUrl()
    logger=LogGen.loggen()

    # @pytest.mark.regression
    def test_searchbyemail(self,setup):
        self.driver=setup
        self.logger.info("*************Test Search customer by email_004*******************")
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("*********Login Successful****************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickcustomer()
        self.addcust.clicksublinkcustomer()
        self.logger.info("******Searching customer by emailID*****")

        self.searchcust=searchcustomer(self.driver)
        self.searchcust.setemail("steve_gates@nopCommerce.com")

        self.searchcust.clicksearch()
        self.logger.info(("******clicking on search***************"))
        time.sleep(3)
        status=self.searchcust.searchByEmail("steve_gates@nopCommerce.com")
        assert True==status
        self.logger.info("***********TC_searchcustomerbyemail_004 finished")
        self.driver.close()


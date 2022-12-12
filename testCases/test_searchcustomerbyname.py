from pageObject.LoginPage import Login
from pageObject.AddCustomer import AddCustomer
from utilities.customLogger import LogGen
from utilities.readproperties import configRead
from pageObject.searchcustomerpage import searchcustomer
import pytest
import time

class Test_SearchCustomerByName_005:
    username=configRead.ReadUsername()
    password=configRead.Readpassword()
    url=configRead.ReadUrl()
    logger=LogGen.loggen()

    # @pytest.mark.regression
    def test_searchbyname(self,setup):
        self.driver=setup
        self.logger.info("*************Test Search customer by name_005*******************")
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
        self.logger.info("******Searching customer by name*****")

        self.searchcust=searchcustomer(self.driver)
        self.searchcust.setfirstname("Victoria")
        self.searchcust.setlastname("Terces")


        self.searchcust.clicksearch()
        time.sleep(3)
        status=self.searchcust.searchByName("Victoria Terces")
        assert True==status
        self.logger.info("***********TC_searchcustomerbyname_005 finished")
        self.driver.close()


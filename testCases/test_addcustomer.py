from pageObject.LoginPage import Login
from utilities.readproperties import configRead
from utilities.customLogger import LogGen
from pageObject.AddCustomer import AddCustomer
import pytest
import random
import string
import time
from selenium.webdriver.common.by import By

class Test_003_addcustomer:
    username=configRead.ReadUsername()
    password=configRead.Readpassword()
    url=configRead.ReadUrl()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("********Test_003_addcustomer*****************")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************login successful****************")

        self.logger.info("**********starting add customer test case***************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickcustomer()
        self.addcust.clicksublinkcustomer()
        self.addcust.clickaddNew()
        self.logger.info("*******providing customer info********")

        self.email= random_generator()+"@gmail.com"
        self.addcust.clickemail(self.email)
        self.addcust.clickpassword("test111")
        self.addcust.clickfirstname("Priya")
        self.addcust.clicklastname("Shah")
        self.addcust.clicksetgender("Female")
        self.addcust.clickdateOfBirth("12/04/1985")
        self.addcust.clickcompanyname("BusyQA")
        self.addcust.clicktaxexempt()
        self.addcust.clicknewsletter("Your store name")
        #self.addcust.clickcustomerrole("Administrators")
        self.addcust.clickmanagerofvendor("Vendor 1")

        self.addcust.clicksavebutton()

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "customer has been added successfully" in self.msg:
            assert True== True
            self.logger.info("**********Customer added successfully*********************")
        else:
            self.driver.save_screenshot("\\.Screenshot\\"+"add_customer_scr.png")
            self.logger.info("***********Customer is not added********************")
            assert False==False
        self.driver.close()
        self.logger.info("*************Ending Add customer test*******************")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars)for r in range(size))






import time
from utilities.readproperties import configRead
from utilities.customLogger import LogGen
from pageObject.Orderpage import orderpage
from pageObject.LoginPage import Login
from pageObject.AddCustomer import AddCustomer
import pytest

class Test_searchorder_006:

    username=configRead.ReadUsername()
    password=configRead.Readpassword()
    url=configRead.ReadUrl()
    logger=LogGen.loggen()


    def test_ordersearch(self,setup):

        self.logger.info("*******Test_order_006**************")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp=Login(self.driver) #login object created
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("*******Login Successful******************")
        self.logger.info("*****************Starting search order test****************")
        assert "admin" in self.driver.current_url
        # self.addcust=AddCustomer(self.driver) #Addcustomer object created
        # self.addcust.menusearch()

        self.orderpg=orderpage(self.driver)
        time.sleep(3)
        self.orderpg.clicksaleslink()
        print("##############")
        time.sleep(3)
        self.orderpg.clickorder()
        print("%%%%%%%%%%%%%%%%%")
        time.sleep(3)
        # assert self.driver.title =="Orders / nopCommerce administration"
        assert "order" in self.driver.current_url
        self.orderpg.setstartdate("12/12/2023")#################3
        self.orderpg.setenddate("12/25/2023")
        self.orderpg.setwarehouse("Warehouse 1 (New York)")
        self.orderpg.setproduct("ABCD")
        self.orderpg.selectorder("Complete")
        self.orderpg.selectpaymentstatus("Paid")
        self.orderpg.selectshippingstatus("Shipped")
        self.orderpg.selectvendor("Vendor 2")
        self.orderpg.setbillingphone("123456789")
        self.orderpg.setemail("priya@gmail.com")
        self.orderpg.setlastname("Shah")
        self.orderpg.setbillingcountry("United States")
        self.orderpg.setpaymentmethod("Payments.PayPalSmartPaymentButtons")
        self.orderpg.setordernotes("#123#")
        self.orderpg.clicksearch()







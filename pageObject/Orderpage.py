from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class orderpage:
    link_sales_xpath="//a[@href='#']//p[contains(text(),'Sales')]"
    select_order_xpath="//a[@href='/Admin/Order/List']"
    txtbox_startdate_xpath="//input[@id='StartDate']"
    txtbox_enddate_xpath="//input[@id='EndDate']"
    drp_warehouseid_xpath="//select[@id='WarehouseId']"
    selectoption1="Warehouse 1 (New York)"
    textbox_product_xpath="//input[@id='search-product-name']"
    textbox_orderstatus_xpath="//ul[@id='OrderStatusIds_taglist']"
    selectitem_processing_xpath="//li[contains(text(),'Processing')]"
    drp_paymentstatus_xpath="//ul[@id='PaymentStatusIds_taglist']"
    drp_shippingstatus_xpath="//ul[@id='ShippingStatusIds_taglist']"
    txtbox_vendor_xpath="//select[@id='VendorId']"
    txtbox_billingphonenumber_xpath="//input[@id='BillingPhone']"
    txtbox_billingemailid_xpath="//input[@id='BillingEmail']"
    txt_billinglastname_xpath="//input[@id='BillingLastName']"
    drp_billingcountry_xpath="//select[@id='BillingCountryId']"
    drp_paymentmethod_xpath="//select[@id='PaymentMethodSystemName']"
    txtbox_ordernotes_xpath="//input[@name='OrderNotes']"
    button_search_xpath="//button[@id='search-orders']"

    def __init__(self,driver):
        self.driver=driver

    def clicksaleslink(self):
        self.driver.find_element(By.XPATH,self.link_sales_xpath)

    def clickorder(self):
        self.driver.find_element(By.XPATH,self.select_order_xpath)

    def setstartdate(self,date):
        self.driver.find_element(By.XPATH,self.txtbox_startdate_xpath).send_keys(date)

    def setenddate(self,date):
        self.driver.find_element(By.XPATH,self.txtbox_enddate_xpath).send_keys(date)

    def setwarehouse(self,option):
        drp=Select(self.driver.find_element(By.XPATH,self.drp_warehouseid_xpath))
        drp.select_by_visible_text(option)

    def setproduct(self,value):
        self.driver.find_element(By.XPATH,self.textbox_product_xpath).send_keys(value)

    def selectorder(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.textbox_orderstatus_xpath))
        drp.select_by_visible_text(value)

    def selectpaymentstatus(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drp_paymentstatus_xpath))
        drp.select_by_visible_text(value)

    def selectshippingstatus(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drp_shippingstatus_xpath))
        drp.select_by_visible_text(value)

    def selectvendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.txtbox_vendor_xpath))
        drp.select_by_visible_text(value)

    def setbillingphone(self,value):
        self.driver.find_element(By.XPATH,self.txtbox_billingphonenumber_xpath).send_keys(value)

    def setemail(self,value):
        self.driver.find_element(By.XPATH,self.txtbox_billingemailid_xpath).send_keys(value)

    def setlastname(self,value):
        self.driver.find_element(By.XPATH,self.txt_billinglastname_xpath).send_keys(value)

    def setbillingcountry(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drp_billingcountry_xpath))
        drp.select_by_visible_text(value)

    def setpaymentmethod(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drp_paymentmethod_xpath))
        drp.select_by_visible_text(value)

    def setordernotes(self,value):
        self.driver.find_element(By.XPATH,self.txtbox_ordernotes_xpath).send_keys(value)

    def clicksearch(self):
        self.driver.find_element(By.XPATH,self.button_search_xpath).click()







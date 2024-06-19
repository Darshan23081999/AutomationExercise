from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AccountRegistrationPage():
    btn_Gender='id_gender1'
    txt_password_id = 'password'
    txt_DOB_date_id='days'
    txt_DOB_month_id='months'
    txt_DOB_year_id = 'years'
    cbox_signup_id='newsletter'
    cbox_Offer_id='optin'
    txt_firstname_name='first_name'
    txt_lastname_name='last_name'
    txt_address_id='address1'
    txt_state_id='state'
    txt_city_id='city'
    txt_zipCode_id='zipcode'
    txt_mobileNo_id='mobile_number'
    clk_createAccount_TagAndAttribute="button[data-qa='create-account']"
    select_Ctry_xpath="//select[@id='country']"
    text_msg_conf_cssSelector="h2[class='title text-center'] b"

    def __init__(self,driver):
        self.driver=driver

    def setGender(self):
        self.driver.find_element(By.ID,self.btn_Gender).click()

    def setPassword(self,pwd):
        self.driver.find_element(By.ID,self.txt_password_id).send_keys(pwd)

    def checkBoxSignup(self):
        self.driver.find_element(By.ID,self.cbox_signup_id).click()

    def checkboxOffer(self):
        self.driver.find_element(By.ID,self.cbox_Offer_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setAddress(self,addrs):
        self.driver.find_element(By.ID,self.txt_address_id).send_keys(addrs)

    def setState(self,state):
        self.driver.find_element(By.ID,self.txt_state_id).send_keys(state)

    def setCity(self,cty):
        self.driver.find_element(By.ID,self.txt_city_id).send_keys(cty)

    def setZipCode(self,zipCode):
        self.driver.find_element(By.ID,self.txt_zipCode_id).send_keys(zipCode)

    def setMobileNo(self,MobileNum):
        self.driver.find_element(By.ID,self.txt_mobileNo_id).send_keys(MobileNum)

    def clickCreateAcc(self):
        self.driver.find_element(By.CSS_SELECTOR,self.clk_createAccount_TagAndAttribute).click()

    def selectCountry(self):
        self.sCtry=self.driver.find_element(By.XPATH,self.select_Ctry_xpath)
        self.ctry=Select(self.sCtry)
        self.ctry.select_by_visible_text("Australia")

    def selectDoB_date(self,date):
        self.date=self.driver.find_element(By.ID,self.txt_DOB_date_id)
        self.sdate=Select(self.date)
        self.sdate.select_by_visible_text(date)

    def selectDoB_month(self,month):
        self.month=self.driver.find_element(By.ID,self.txt_DOB_month_id)
        self.smonth=Select(self.month)
        self.smonth.select_by_visible_text(month)

    def selectDoB_year(self,year):
        self.year=self.driver.find_element(By.ID,self.txt_DOB_year_id)
        self.syear=Select(self.year)
        self.syear.select_by_visible_text(year)

    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR,self.text_msg_conf_cssSelector).text
        except:
            None
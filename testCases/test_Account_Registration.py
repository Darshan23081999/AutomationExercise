import os
from pageObjects.homePage import HomePage
from pageObjects.accountRegistrationPage import AccountRegistrationPage
from utilities.randomString import randomStringGenerator
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

# pytest - v - s.\Pytest\PageObjectModel\testOpencartLogin.py
#  pytest -v -s .\testCases\test_Account_Registration.py
# pip install -U -r requirements.txt

class Test001Accountreg:
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    # baseURL = "https://automationexercise.com/signup"

    def test_account_reg(self, setup):
        self.logger.info("** Test__001_AccountRegistration Started **")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching Application")
        self.driver.maximize_window()
        # self.driver.close()

        self.hp=HomePage(self.driver)
        self.hp.clickSignUpORLogin()
        self.hp.setName("KKK")
        # self.hp.setEmail("stda@gmail.com")
        setEmail=randomStringGenerator()+'@gmail.com'
        self.hp.setEmail(setEmail)
        self.hp.clickSignup()

        self.ar= AccountRegistrationPage(self.driver)
        self.ar.setGender()
        self.ar.setPassword("hdkfhkj")
        self.ar.selectDoB_date('23')
        self.ar.selectDoB_month('August')
        self.ar.selectDoB_year("1999")
        self.ar.checkBoxSignup()
        self.ar.checkboxOffer()
        self.ar.setFirstName('HHHH')
        self.ar.setLastName("j")
        self.ar.setAddress("kajshfkjhakjs")
        self.ar.selectCountry()
        self.ar.setState("Kar")
        self.ar.setCity("Nel")
        # self.ar.setZipCode("56345")
        # self.ar.setMobileNo("9113261921")
        self.ar.clickCreateAcc()
        self.confmsg=self.ar.getConfirmationMsg()
        if self.confmsg == 'ACCOUNT CREATED!':
            self.logger.info("AccountRegistration Passed")
            assert True
            self.driver.close()

        else:
            # self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "llllll.png") #will not work
            # self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\" + "test_account_reg.png")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\test_Account.png")
            self.logger.error("AccountRegistration Failed")
            self.driver.close()
            assert False
        self.logger.info("** Test__001_AccountRegistration Finished **")


# from pageObjects.homePage import HomePage
# from pageObjects.accountRegistrationPage import AccountRegistrationPage

# class Test_001_AccountReg:
#     baseURL = "https://demo.opencart.com/"
#
#     def test_account_reg(self,setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
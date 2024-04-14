import os
from selenium import webdriver
from pageObjects.homePage import HomePage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_02_login:

    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    lemail=ReadConfig.getUsername()
    lpwd=ReadConfig.getPassword()

    def test_login(self,setup):
        self.logger.info("Test02 LOgin page started ")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("application is launghing")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickSignUpORLogin()
        self.logger.info("Login through credentials")
        self.hp.setLoginEmail(self.lemail)
        self.hp.setLoginPassword(self.lpwd)
        self.hp.clkLogin()
        self.targetpage= self.hp.LoginSuccess_msg()
        if self.targetpage == True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+'\\screenshots\\'+'test_login.png')
            assert False
        self.driver.close()
        self.logger.info("End of TC02")



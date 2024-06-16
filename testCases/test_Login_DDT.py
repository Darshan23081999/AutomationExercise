import os
import time

from selenium import webdriver
from pageObjects.homePage import HomePage
from pageObjects.accountRegistrationPage import AccountRegistrationPage
from pageObjects.myaccountpage import MyAccountpage
from utilities import XLUtils
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test03_login_DTT:
    baseurl = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    path = os.path.abspath(os.curdir) + '\\testData\\Opencart_LoginData.xlsx'

    def test_login_dtt(self, setup):
        self.logger.info('starting test3 login datadriven')
        self.row = XLUtils.getRowCount(self.path, 'sheet1')
        lst_status = []
        self.driver = setup

        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.ar = AccountRegistrationPage(self.driver)
        self.ma = MyAccountpage(self.driver)
        self.logger.info('Getting the data from Excel file')
        for r in range(2, self.row + 1):
            self.hp.clickSignUpORLogin()
            self.email = XLUtils.readData(self.path, 'sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)
            self.hp.setLoginEmail(self.email)
            self.hp.setLoginPassword(self.password)
            self.hp.clkLogin()
            time.sleep(5)
            self.targetpage = self.hp.LoginSuccess_msg()
            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append('pass')
                    self.myaccountpage.clkLogout()
                else:
                    lst_status.append('fail')
            elif self.exp == 'Invalid':
                if self.tragetpage==True:
                    lst_status.append('fail')
                else:
                    lst_status.append('pass')
        self.driver.close()
        if 'fail' not in lst_status:
            assert True
        else:
            assert False
        self.logger.info('**End of test03_DDT**')

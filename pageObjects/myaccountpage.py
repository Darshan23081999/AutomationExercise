from selenium import webdriver
from selenium.webdriver.common.by import By

class MyAccountpage():
    txt_logout='Logout'

    def __init__(self,driver):
        self.driver = driver

    def clkLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.txt_logout).click()

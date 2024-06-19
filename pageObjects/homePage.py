# https://automationexercise.com/
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage():
    lnk_signUpORLogin = 'Signup / Login'
    txt_signupName_xpath = "//input[@placeholder='Name']"
    txt_signupEmail_xpath = "//input[@data-qa='signup-email']"
    txt_signupButton_xpath = "//button[normalize-space()='Signup']"
    txt_login_email_name = 'email'
    txt_login_password_name = 'password'
    clk_login_btn_type= 'button[type=submit]'
    txt_login_success='Logged in as'

    def __init__(self, driver):
        self.driver = driver

    def clickSignUpORLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_signUpORLogin).click()

    def setName(self, signUpName):
        self.driver.find_element(By.XPATH, self.txt_signupName_xpath).send_keys(signUpName)

    def setEmail(self, signupEmail):
        self.driver.find_element(By.XPATH, self.txt_signupEmail_xpath).send_keys(signupEmail)

    def clickSignup(self):
        self.driver.find_element(By.XPATH, self.txt_signupButton_xpath).click()

    def setLoginEmail(self,lemail):
        self.driver.find_element(By.NAME, self.txt_login_email_name).send_keys(lemail)

    def setLoginPassword(self,lpwd):
        self.driver.find_element(By.NAME, self.txt_login_password_name).send_keys(lpwd)

    def clkLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.clk_login_btn_type).click()

    def LoginSuccess_msg(self):
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT,self.txt_login_success).is_displayed()
            return True
        except:
            return False

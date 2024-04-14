import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://automationexercise.com")
# driver.get("https://www.opencart.com/index.php?route=account/register")
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.implicitly_wait(10)

# driver.find_element(By.LINK_TEXT, "Signup / Login").click()
# driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("hhhh")
# driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("sjdshgfkj@gmail.com")
# driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()
# s = Select(driver.find_element(By.XPATH, "//select[@id='country']/option"))
# s = Select(driver.find_element(By.XPATH, "//select[@id='input-country']/option"))
dropdown=Select(driver.find_element(By.XPATH,"//select[@id='Skills']"))
dropdown.select_by_visible_text("Adobe InDesign")
# ctry = Select(s)
# print(s)
# s.select_by_visible_text("Australia")
# s.select_by_visible_text("Australia")
# d=driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"nnnnnn.png")
d=driver.save_screenshot(os.path.abspath(os.curdir)+ "\\screenshots\\" + "uuuuuuuuuu.png")
print(d)
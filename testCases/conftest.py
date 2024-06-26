import os
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser")
    elif browser == 'firefox':
        driver=webdriver.Firefox(GeckoDriverManager().install())
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome browser")
    return driver

def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):   # This will return the Browser value to setup method
    return request.config.getoption("--browser")
# pytest -s -v .\testCases\test_Account_Registration.py --browser edge

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'AutomationExercise'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Darshan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
# pytest -s -v .\testCases\test_Account_Registration.py --html=reports\report.html --capture=tee-sys

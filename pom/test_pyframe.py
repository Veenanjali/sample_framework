import pytest
from selenium import webdriver
from frame import LoginPage
from selenium.webdriver.chrome.options import Options
obj = Options()
#obj.add_experimental_option("detach",True)
obj.add_argument('--headless')
chrome_driver_path ="/usr/local/bin/chromedriver"
from  time import *

@pytest.fixture
def setup():
    # Initialize WebDriver
    driver = webdriver.Chrome(executable_path=chrome_driver_path,options=obj)
    yield driver
    # Cleanup after test execution
    driver.quit()

def test_successful_login(setup):
    login_page = LoginPage(setup)
    login_page.open()
    sleep(2)
    login_page.enter_username('student')
    login_page.enter_password('Password123')
    login_page.click_login_button()
    #assert login_page.is_logged_in()

def test_invalid_login(setup):
    login_page = LoginPage(setup)
    login_page.open()
    sleep(5)
    login_page.enter_username('invalid_user@example.com')
    login_page.enter_password('invalid_password')
    login_page.click_login_button()
    sleep(2)
    assert login_page.is_error_displayed()

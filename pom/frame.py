from pom.locators import Locate
from selenium.webdriver.common.by import By

class LoginPage:
    # Locators

    def __init__(self, driver):
        self.driver = driver
        self.l1 = Locate()
    def open(self):
        self.driver.get(self.l1.URL)

    def enter_username(self, username):
        self.driver.find_element(By.XPATH,self.l1.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME,self.l1.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.TAG_NAME,self.l1.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return 'Welcome' in self.driver.title

    def is_error_displayed(self):
        return self.driver.find_element(By.TAG_NAME,self.l1.ERROR_MESSAGE).is_displayed()

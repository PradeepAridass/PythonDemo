from selenium.webdriver.common.by import By

from Pages.ShopPage import ShopPage
from Utils.BrowserUtils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.useName = (By.ID, "username")
        # self.password = (By.NAME, "password")
        # self.signIn = (By.ID, "signInBtn")

    def login(self, userName, password):
        # self.driver.find_element(*self.useName).send_keys(userName)
        # self.driver.find_element(*self.password).send_keys(password)
        # self.driver.find_element(*self.signIn).click()
        shopPage = ShopPage(self.driver)
        return shopPage
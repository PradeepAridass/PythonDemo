from selenium.webdriver.common.by import By

from Pages.Checkout_Confirmation import Checkout_Confirmation
from Utils.BrowserUtils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.addCart = (By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def product_list(self, product_name):
        self.driver.find_element(*self.shop_link).click()
        cards = self.driver.find_elements(*self.product_cards)
        # addToCart = self.driver.find_element(By.XPATH, "//div[@class='card-footer']/button")
        for card in cards:
            productName = card.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                print(productName)
                card.find_element(By.XPATH, "div/button").click()

    def goToCart(self):
        self.driver.find_element(*self.addCart).click()
        checkout_confirm = Checkout_Confirmation(self.driver)
        return checkout_confirm
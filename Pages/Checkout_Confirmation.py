from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:
    def __init__(self, driver):
        self.driver = driver
        self.checkoutButton = (By.XPATH, "//tbody/tr[3]/td[5]")
        self.countryInput = (By.ID, "country")
        self.countryOption = (By.LINK_TEXT, "India")
        self.checkBox = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
        self.submitButton = (By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")
        self.success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def checkout(self):
        self.driver.find_element(*self.checkoutButton).click()


    def delivery_address(self, countryName):
        self.driver.find_element(*self.countryInput).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.countryOption))
        self.driver.find_element(*self.countryOption).click()
        # countries = driver.find_elements(By.CSS_SELECTOR, "div[class='suggestions'] ul li a")
        # for country in self.countryOption:
        #     if country.text == count:
        #         country.click()
        #         break
        # time.sleep(2)
        self.driver.find_element(*self.checkBox).click()
        self.driver.find_element(*self.submitButton).click()


    def validate_order(self):
        successMsg = self.driver.find_element(*self.success_message).text
        # assert successMsg == 'Success! Thank you! Your order will be delivered in next few weeks :-).'
        assert "Success! Thank you!" in successMsg
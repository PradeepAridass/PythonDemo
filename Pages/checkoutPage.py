from Frame.conftest import driver
from Utils.BrowserUtils import BrowserUtils


class CheckoutPage(BrowserUtils):
    def __init__(self):
        super().__init__(driver)
        self.driver= driver

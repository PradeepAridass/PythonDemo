
# pytest -m smoke //tagging > to run specific file using tags (E.g.: smoke)
# pytest -n 5 // to run the file parallel
# pytest -n 2 -m smoke --browser_name firefox --html=Frame/reports/report.html

import json
import os
import sys

import pytest

from Pages.LoginPage import LoginPage

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

test_dataPath = '../Datas/test_data.json'
with open(test_dataPath) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_data_list", test_list)
def test_e2e(browserInitialise, test_data_list):
    driver = browserInitialise
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shopPage = loginPage.login(test_data_list["userEmail"], test_data_list["userPassword"])
    shopPage.product_list(test_data_list["productName"])
    print(shopPage.getTitle())
    checkout_confirm = shopPage.goToCart()
    checkout_confirm.checkout()
    checkout_confirm.delivery_address(test_data_list["countryName"])
    checkout_confirm.validate_order()





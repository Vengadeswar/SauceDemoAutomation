import time

from Config.config import USERNAME, PASSWORD, EXCEL_PATH
from Pages.LoginPage import LoginPage
import pytest
from utils.excel_reading import read_excel


@pytest.mark.usefixtures("setup")
class TestInventory:

    def test_verify_count_of_products_in_home_page(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login(USERNAME,PASSWORD)
        homepage.verify_presence_of_app_logo()
        assert homepage.return_products_count() == 6

    def test_low_to_high_price_sorting(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login(USERNAME,PASSWORD)
        homepage.verify_presence_of_app_logo()
        homepage.select_option_in_sort_dropdown("Price (low to high)")
        act_prices = homepage.products_price()
        exp_prices = sorted(act_prices)
        assert act_prices==exp_prices,"Prices are not sorted in low to high"

    def test_logout(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login(USERNAME,PASSWORD)
        homepage.verify_presence_of_app_logo()
        homepage.click_burger_menu()
        homepage.click_logout()
        assert loginpage.verify_presence_of_username_text()

    def test_add_multiple_products(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login(USERNAME,PASSWORD)
        homepage.verify_presence_of_app_logo()
        products = read_excel(EXCEL_PATH)
        homepage.add_multiple_products(products)
        assert homepage.prod_count_in_cart() == str(len(products))

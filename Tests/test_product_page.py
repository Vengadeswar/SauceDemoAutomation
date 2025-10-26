from Config.config import USERNAME1, PASSWORD
from Pages.LoginPage import LoginPage
import pytest

@pytest.mark.usefixtures("setup")
class TestProductPage:

    @pytest.mark.skip("Skipping as its failing due to data issue")
    def test_single_product_details(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login(USERNAME1,PASSWORD)
        homepage.verify_presence_of_app_logo()
        prod_page = homepage.click_on_a_product("Sauce Labs Bolt T-Shirt")
        assert prod_page.verify_presence_of_prod_name()
        assert prod_page.verify_presence_of_prod_price()
        assert prod_page.verify_presence_of_image()

    @pytest.mark.skip("Skipping as its failing due to data issue")
    def test_adding_product_to_cart_in_inventory(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login(USERNAME1,PASSWORD)
        homepage.verify_presence_of_app_logo()
        prod_page = homepage.click_on_a_product("Sauce Labs Onesie")
        prod_page.add_prod_to_cart()
        count = prod_page.prod_count_in_cart()
        assert count == '1'

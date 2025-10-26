from Config.config import USERNAME, PASSWORD
from Pages.LoginPage import LoginPage
import pytest

@pytest.mark.usefixtures("setup")
class TestCartPage:

    def test_adding_product_to_cart(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login(USERNAME, PASSWORD)
        homepage.verify_presence_of_app_logo()
        prod_page = homepage.click_on_a_product("Sauce Labs Onesie")
        prod_page.add_prod_to_cart()
        cartpage = prod_page.go_to_cart()
        infopage = cartpage.proceed_checkout()
        assert infopage.verify_presence_of_your_info_text()

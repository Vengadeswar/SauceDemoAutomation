from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.CartPage import CartPage


class ProductPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.prod_price = (By.CSS_SELECTOR,".inventory_details_price")
        self.prod_name = (By.CSS_SELECTOR,".inventory_details_name")
        self.add_to_cart = (By.ID,"add-to-cart")
        self.image = (By.CSS_SELECTOR,".inventory_details_img")
        self.prod_count = (By.CSS_SELECTOR,".shopping_cart_badge")
        self.cart_btn = (By.CSS_SELECTOR,".shopping_cart_link")

    def verify_presence_of_prod_name(self):
        return self.is_displayed(self.prod_name)

    def verify_presence_of_prod_price(self):
        return self.is_displayed(self.prod_price)

    def verify_presence_of_image(self):
        return self.is_displayed(self.image)

    def add_prod_to_cart(self):
        return self.click(self.add_to_cart)

    def prod_count_in_cart(self):
        return self.get_text(self.prod_count)

    def go_to_cart(self):
        self.click(self.cart_btn)
        cartpage = CartPage(self.driver)
        return cartpage

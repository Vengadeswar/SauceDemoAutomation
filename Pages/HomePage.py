from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.ProductPage import ProductPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.app_logo = (By.CSS_SELECTOR,".app_logo")
        self.prod_tile = (By.CSS_SELECTOR,".inventory_item_name")
        self.sort_dropdown = (By.CSS_SELECTOR,".product_sort_container")
        self.price = (By.CSS_SELECTOR,".inventory_item_price")
        self.prod_name = (By.CSS_SELECTOR,".inventory_item_name")
        self.burger_menu = (By.ID,"react-burger-menu-btn")
        self.logout_button = (By.ID,"logout_sidebar_link")
        self.prod_count = (By.CSS_SELECTOR, ".shopping_cart_badge")


    def verify_presence_of_app_logo(self):
        assert self.is_displayed(self.app_logo)

    def return_products_count(self):
        return len(self.find_elements(self.prod_tile))

    def select_option_in_sort_dropdown(self,option):
        self.select_option(self.sort_dropdown,option)

    def products_price(self):
        elements = self.find_elements(self.price)
        price_lst = []
        for ele in elements:
             price_lst.append(float(self.get_text(ele).replace("$","")))
        return price_lst

    def click_on_a_product(self,name):
        names = self.find_elements(self.prod_name)
        for i in names:
            if i.text == name:
                self.click(i)
                break
        self.dismiss_alert()
        product_page = ProductPage(self.driver)
        return product_page

    def click_burger_menu(self):
        self.click(self.burger_menu)
        self.dismiss_alert()

    def click_logout(self):
        self.click(self.logout_button)

    def add_multiple_products(self,name_list):
        products = self.find_elements(self.prod_tile)
        for prod in products:
            if prod.text in name_list:
                dynamic_xpath = f"//div[text()='{prod.text}']/ancestor::div[@class='inventory_item']//button"
                self.click((By.XPATH,dynamic_xpath))

    def prod_count_in_cart(self):
        return self.get_text(self.prod_count)
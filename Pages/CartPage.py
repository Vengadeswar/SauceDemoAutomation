from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.InfoPage import InfoPage


class CartPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout = (By.ID,"checkout")
        self.remove = (By.XPATH,"//button[text()='Remove']")

    def proceed_checkout(self):
        self.click(self.checkout)
        infopage = InfoPage(self.driver)
        return infopage

    def remove_item(self):
        self.click(self.remove)

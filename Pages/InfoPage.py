from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class InfoPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.your_info_text = (By.XPATH,"//span[text()='Checkout: Your Information']")

    def verify_presence_of_your_info_text(self):
        return self.is_displayed(self.your_info_text)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def find_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self,locator):
        if isinstance(locator,tuple):
            element = self.find_element(locator)
        else:
            element = locator
        element.click()

    def send_keys(self,locator,text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    def is_displayed(self,locator):
       return self.find_element(locator).is_displayed()

    def get_text(self,locator):
        if isinstance(locator, tuple):
            element = self.find_element(locator)
        else:
            element = locator
        return element.text

    def select_option(self,locator,option):
        drp_down = Select(self.find_element(locator))
        drp_down.select_by_visible_text(option)


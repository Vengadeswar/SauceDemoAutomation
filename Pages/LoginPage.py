from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.user_name = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_msg = (By.CSS_SELECTOR, ".error-message-container")
        self.accepted_username_text = (By.XPATH,"//h4[text()='Accepted usernames are:']")

    def type_username(self,username):
        self.send_keys(self.user_name,username)

    def type_password(self,password):
        self.send_keys(self.password,password)

    def click_login_button(self):
        self.click(self.login_button)

    def verify_presence_of_error_msg(self):
        assert self.is_displayed(self.error_msg)

    def login(self,username,password):
        self.type_username(username)
        self.type_password(password)
        self.click_login_button()
        self.dismiss_alert()
        homepage = HomePage(self.driver)
        return homepage

    def get_error_msg(self):
        return self.get_text(self.error_msg)

    def verify_presence_of_username_text(self):
        return self.is_displayed(self.accepted_username_text)

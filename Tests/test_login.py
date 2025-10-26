import pytest
from Pages.LoginPage import LoginPage
from TestData.login_data import valid_creds, invalid_username_creds, invalid_password_creds


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("creds",valid_creds)
    def test_valid_login(self,creds):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login(creds['username'],creds['password'])
        homepage.verify_presence_of_app_logo()

    def test_invalid_login_invalid_username(self):
        loginpage = LoginPage(self.driver)
        loginpage.login(invalid_username_creds['username'],invalid_username_creds['password'])
        loginpage.verify_presence_of_error_msg()

    def test_invalid_login_invalid_password(self):
        loginpage = LoginPage(self.driver)
        loginpage.login(invalid_password_creds['username'], invalid_password_creds['password'])
        loginpage.verify_presence_of_error_msg()

    def test_invalid_login_empty_username_password(self):
        loginpage = LoginPage(self.driver)
        loginpage.click_login_button()
        assert loginpage.get_error_msg()=="Epic sadface: Username is required"

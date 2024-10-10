import pytest
from pageobjects.home_page import HomePage
from tests.base_test import BaseTest
from utilities import excel_utils


class TestLogin(BaseTest):
    @pytest.mark.parametrize("email, psw", excel_utils.get_all_excel_data("login_test"))     # data driven testing
    def test_login_valid_cred(self, email, psw):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_with_credentials(email, psw)
        assert account_page.is_account_info_text_displayed()

    def test_login_invalid_mail_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials(self.generate_mail(), "qwerty456")
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed().__contains__(exp_warn_msg)

    def test_login_valid_mail_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("test_1@gmail.com", "453453")
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed().__contains__(exp_warn_msg)

    def test_login_without_cred(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("", "")
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed().__contains__(exp_warn_msg)
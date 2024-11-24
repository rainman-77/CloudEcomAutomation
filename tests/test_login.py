import logging
import pytest
from pageobjects.home_page import HomePage
from tests.base_test import BaseTest
from utilities import excel_utils


@pytest.mark.order(2)  # Set the desired order for this test file
class TestLogin(BaseTest):
    @pytest.mark.parametrize("data", excel_utils.get_all_excel_data("login_test"))     # data driven testing
    def test_login_valid_cred(self, data):
        logging.info(f"test_login--> test_login_valid_cred started using {data['email']}")

        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_with_credentials(data["email"], data["password"])
        assert account_page.is_account_info_text_displayed()

        logging.info("test_login--> test_login_valid_cred completed\n")

    def test_login_invalid_mail_and_valid_password(self):
        logging.info("test_login--> test_login_invalid_mail_and_valid_password started")

        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials(self.generate_mail(), "qwerty456")
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed().__contains__(exp_warn_msg)

        logging.info("test_login--> test_login_invalid_mail_and_valid_password completed\n")

    def test_login_valid_mail_and_invalid_password(self):
        logging.info("test_login--> test_login_valid_mail_and_invalid_password started")

        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("test_1@gmail.com", "453453")
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed().__contains__(exp_warn_msg)

        logging.info("test_login--> test_login_valid_mail_and_invalid_password completed\n")

    def test_login_without_cred(self):
        logging.info("test_login--> test_login_without_cred started")

        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("", "")
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed().__contains__(exp_warn_msg)

        logging.info("test_login--> test_login_without_cred completed\n")
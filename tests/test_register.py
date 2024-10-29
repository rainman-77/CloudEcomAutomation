import logging
import pytest
from pageobjects.home_page import HomePage
from tests.base_test import BaseTest
from utilities import excel_utils


@pytest.mark.order(3)  # Set the desired order for this test file
class TestRegister(BaseTest):
    def test_register_mandatory_fields(self):
        logging.info("test_register--> test_register_mandatory_fields started")

        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        firstname = excel_utils.get_cell_data("register_test", 2, 1)    # using testdata from excel
        lastname = excel_utils.get_cell_data("register_test", 2, 2)
        account_success_page = register_page.register_account(firstname, lastname, self.generate_mail(), "32423", "qwerty456", "qwerty456", "no", "yes")
        exp_txt = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_created_msg().__eq__(exp_txt)

        logging.info("test_register--> test_register_mandatory_fields completed\n")

    def test_register_all_fields(self):
        logging.info("test_register--> test_register_all_fields started")

        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_account("testing", "2", self.generate_mail(), "32423", "qwerty456", "qwerty456", "yes", "yes")
        exp_txt = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_created_msg().__eq__(exp_txt)

        logging.info("test_register--> test_register_all_fields completed\n")

    def test_register_existing_mail(self):
        logging.info("test_register--> test_register_existing_mail started")

        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_account("testing", "2", "test_1@gmail.com", "32423", "qwerty456", "qwerty456", "no", "yes")
        exp_txt = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_warning_msg().__contains__(exp_txt)

        logging.info("test_register--> test_register_existing_mail completed\n")

    def test_register_without_anyfields(self):
        logging.info("test_register--> test_register_without_anyfields started")

        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_account("", "", "", "", "", "", "no", "no")
        exp_privacy_policy_msg = "Warning: You must agree to the Privacy Policy!"
        exp_frs_name_warn_msg = "First Name must be between 1 and 32 characters!"
        exp_lst_name_warn_msg = "Last Name must be between 1 and 32 characters!"
        exp_email_warn_msg = "E-Mail Address does not appear to be valid!"
        exp_phone_warn_msg = "Telephone must be between 3 and 32 characters!"
        exp_pswd_warn_msg = "Password must be between 4 and 20 characters!"

        expected_warning_msgs = [exp_privacy_policy_msg, exp_frs_name_warn_msg,
                                 exp_lst_name_warn_msg, exp_email_warn_msg,
                                 exp_phone_warn_msg, exp_pswd_warn_msg]
        msg_compare_results = register_page.verify_warning_msgs(expected_warning_msgs)
        for x in range(len(msg_compare_results)):
            assert msg_compare_results[x], f"expected warning message not coming:{expected_warning_msgs[x]}"

        logging.info("test_register--> test_register_without_anyfields completed\n")


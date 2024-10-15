from pageobjects.account_success_page import AccountSuccessPage
from pageobjects.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_id = {"id": "input-firstname"}
    last_name_id = {"id": "input-lastname"}
    mail_id = {"id": "input-email"}
    telephone_id = {"id": "input-telephone"}
    password_id = {"id": "input-password"}
    confirm_password_id = {"id": "input-confirm"}
    agree_field_name = {"name": "agree"}
    continue_button_xpath = {"xpath": "//input[@value='Continue']"}
    yes_newsletter_xpath = {"xpath": "//input[@name='newsletter'][1]"}
    warning_msg_xpath = {"xpath": "//div[contains(@class,'alert-danger')]"}  # warning message
    firstname_warning_msg_xpath = {"xpath": "//input[@id='input-firstname']/following-sibling::div"}
    lastname_warning_msg_xpath = {"xpath": "//input[@id='input-lastname']/following-sibling::div"}
    email_warning_msg_xpath = {"xpath": "//input[@id='input-email']/following-sibling::div"}
    telephone_warning_msg_xpath = {"xpath": "//input[@id='input-telephone']/following-sibling::div"}
    password_warning_msg_xpath = {"xpath": "//input[@id='input-password']/following-sibling::div"}

    # methods for basic actions
    def enter_first_name(self, firstname):
        self.type_into_element(firstname, self.first_name_id)

    def enter_last_name(self, lastname):
        self.type_into_element(lastname, self.last_name_id)

    def enter_mailid(self, mail):
        self.type_into_element(mail, self.mail_id)

    def enter_telephone_num(self, telephone_num):
        self.type_into_element(telephone_num, self.telephone_id)

    def enter_password(self, password):
        self.type_into_element(password, self.password_id)

    def confirm_password(self, confirm_password):
        self.type_into_element(confirm_password, self.confirm_password_id)

    def subscribe_to_newsletter(self):
        self.element_click(self.yes_newsletter_xpath)

    def click_on_agree(self):  # privacy policy
        self.element_click(self.agree_field_name)

    def click_on_continue(self):
        self.element_click(self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def retrieve_warning_msg(self):        # both existing mail and privacy policy warnings comes here
        return self.get_element_text(self.warning_msg_xpath)

    def retrieve_firstname_warning_msg(self):
        return self.get_element_text(self.firstname_warning_msg_xpath)

    def retrieve_lastname_warning_msg(self):
        return self.get_element_text(self.lastname_warning_msg_xpath)

    def retrieve_email_warning_msg(self):
        return self.get_element_text(self.email_warning_msg_xpath)

    def retrieve_telephone_warning_msg(self):
        return self.get_element_text(self.telephone_warning_msg_xpath)

    def retrieve_password_warning_msg(self):
        return self.get_element_text(self.password_warning_msg_xpath)

    # methods for high level actions
    def register_account(self, firstname, lastname, mail, telephone_num, password, confirm_password,
                         newsletter_yes_or_no, privacy_policy_yes_or_no):
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_mailid(mail)
        self.enter_telephone_num(telephone_num)
        self.enter_password(password)
        self.confirm_password(confirm_password)
        if newsletter_yes_or_no == "yes":
            self.subscribe_to_newsletter()
        if privacy_policy_yes_or_no == "yes":
            self.click_on_agree()
        return self.click_on_continue()

    def verify_warning_msgs(self, expected_warning_msgs):   # order and number of msgs should match with exp and actual
        actual_warning_msgs = [self.retrieve_warning_msg(),
                               self.retrieve_firstname_warning_msg(),
                               self.retrieve_lastname_warning_msg(),
                               self.retrieve_email_warning_msg(),
                               self.retrieve_telephone_warning_msg(),
                               self.retrieve_password_warning_msg()]

        result = []
        for i in range(len(expected_warning_msgs)):
            if expected_warning_msgs[i] == actual_warning_msgs[i]:
                result.append(True)
            else:
                result.append(False)

        return result

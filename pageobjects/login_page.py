from selenium.webdriver.common.by import By

from pageobjects.account_page import AccountPage
from pageobjects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_field_id = {"id": "input-email"}
    password_field_id = {"id": "input-password"}
    login_button_xpath = {"xpath": "//input[@value='Login']"}
    error_message_xpath = {"xpath": "//div[@id='account-login']/div[1]"}

    def enter_email_address(self, email):
        self.type_into_element(email, self.email_field_id)

    def enter_password(self, password):
        self.type_into_element(password, self.password_field_id)

    def click_login_button(self):
        self.element_click(self.login_button_xpath)
        return AccountPage(self.driver)

    def is_error_message_displayed(self):
        return self.get_element_text(self.error_message_xpath)


    def login_with_credentials(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)
        return self.click_login_button()

from selenium.webdriver.common.by import By

from pageobjects.base_page import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    acc_creation_message_xpath = {"xpath": "//div[@id='content']/h1"}

    def retrieve_account_created_msg(self):
        return self.get_element_text(self.acc_creation_message_xpath)


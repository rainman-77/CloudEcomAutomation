from selenium.webdriver.common.by import By

from pageobjects.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_HP_product_link_text = {"link_text": "HP LP3065"}
    no_product_message_xpath = {"xpath": "//input[@id='button-search']/following-sibling::p"}

    def display_status_of_valid_product(self):
        return self.element_display_status(self.valid_HP_product_link_text)

    def retrieve_no_product_message(self):
        return self.get_element_text(self.no_product_message_xpath)


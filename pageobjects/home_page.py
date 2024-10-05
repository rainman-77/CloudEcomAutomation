from pageobjects.base_page import BasePage
from pageobjects.search_page import SearchPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = {"name": "search"}
    search_button_xpath = {"xpath": "//button[contains(@class, 'btn-default')]"}
    myaccount_dropdown_menu_xpath = {"xpath": "//span[text()='My Account']"}

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name, self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click(self.search_button_xpath)
        return SearchPage(self.driver)

    def click_on_myaccount_dropdown_menu(self):
        self.element_click(self.myaccount_dropdown_menu_xpath)

    def search_for_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

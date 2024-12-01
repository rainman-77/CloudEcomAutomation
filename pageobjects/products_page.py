import time

from pageobjects.base_page import BasePage
from pageobjects.product_specific_page import ProductSpecificPage


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    products_xpath = {"xpath": "//span[contains(text(), 'Add to Cart')]"}
    hp_product_link_text = {"link_text": "HP LP3065"}
    macbook_product_link_text = {"link_text": "MacBook"}
    apple_cinema_product_link_text = {"link_text": 'Apple Cinema 30"'}
    iphone_product_link_text = {"link_text": 'iPhone'}
    product_added_success_msg_xpath = {"xpath": "//div[contains(text(), ' Success: You have added ')]"}
    products_name_xpath = {"xpath": "//div[@class='product-thumb']//div[@class='caption']//a"}

    # methods for basic actions
    def click_add_to_product(self, positions):
        for pos in positions:
            time.sleep(1)
            self.elements_click_by_index(self.products_xpath, pos-1)

    def click_on_product_without_mandatory_fields(self):
        self.element_click(self.macbook_product_link_text)
        return ProductSpecificPage(self.driver)

    def click_on_product_with_mandatory_delivery_date(self):
        self.element_click(self.hp_product_link_text)
        return ProductSpecificPage(self.driver)

    def click_on_out_of_stock_product(self):
        self.element_click(self.iphone_product_link_text)
        return ProductSpecificPage(self.driver)

    def click_on_out_of_stock_minimum_order_product(self):
        self.element_click(self.apple_cinema_product_link_text)
        return ProductSpecificPage(self.driver)

    def is_product_added_success_msg_displayed(self):
        return self.element_display_status(self.product_added_success_msg_xpath)

    def get_product_name(self, positions):
        product_names = []
        for pos in positions:
            product_name = self.get_elements_text_by_index(self.products_name_xpath, pos-1)
            product_names.append(product_name)
        return product_names

    # methods for high level actions
    def add_product_and_confirm_success_msg(self, product_position):
        self.click_add_to_product(product_position)
        return self.is_product_added_success_msg_displayed()


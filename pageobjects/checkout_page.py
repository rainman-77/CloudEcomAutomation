import logging
import time
from pageobjects.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    payment_address_radio_buttons_xpath = {"xpath": "//div[@class='radio']//input"}
    payment_address_continue_button_id = {"id": "button-payment-address"}
    payment_address_firstname_id = {"id": "input-payment-firstname"}
    payment_address_lastname_id = {"id": "input-payment-lastname"}
    payment_address_id = {"id": "input-payment-address-1"}
    payment_address_city_id = {"id": "input-payment-city"}
    payment_address_postal_code_id = {"id": "input-payment-postcode"}
    payment_address_country_id = {"id": "input-payment-country"}
    payment_address_region_id = {"id": "input-payment-zone"}

    shipping_address_continue_button_id = {"id": "button-shipping-address"}
    shipping_method_continue_button_id = {"id": "button-shipping-method"}
    agree_checkbox_xpath = {"xpath": "//input[@type='checkbox']"}
    payment_method_continue_button_id = {"id": "button-payment-method"}
    confirm_order_button_id = {"id": "button-confirm"}
    order_success_msg_xpath = {"xpath": "//div[@id='content']//h1"}

    def add_order_details_and_checkout(self, data):
        time.sleep(1)
        radio_buttons_count = self.get_elements_count(self.payment_address_radio_buttons_xpath)

        if radio_buttons_count > 0:     # if existing order details is present then continue
            self.element_click(self.payment_address_continue_button_id)
        else:                           # otherwise add order details
            time.sleep(1)   # waiting for next element loading
            self.type_into_element(data["first_name"], self.payment_address_firstname_id)
            self.type_into_element(data["last_name"], self.payment_address_lastname_id)
            self.type_into_element(data["address"], self.payment_address_id)
            self.type_into_element(data["city"], self.payment_address_city_id)
            self.type_into_element(data["post_code"], self.payment_address_postal_code_id)
            self.select_dropdown_option_by_text(self.payment_address_country_id, data["country"])
            time.sleep(1)   # waiting for next element loading
            self.select_dropdown_option_by_text(self.payment_address_region_id, data["region"])
            self.element_click(self.payment_address_continue_button_id)
        self.element_click(self.shipping_address_continue_button_id)
        self.element_click(self.shipping_method_continue_button_id)
        self.element_click(self.agree_checkbox_xpath)
        self.element_click(self.payment_method_continue_button_id)
        self.element_click(self.confirm_order_button_id)
        time.sleep(1)      # waiting for next element loading
        return self.get_element_text(self.order_success_msg_xpath)



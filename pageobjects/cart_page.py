import logging
import time
from pageobjects.base_page import BasePage
from pageobjects.checkout_page import CheckoutPage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    cart_product_remove_button_xpath = {"xpath": "//button[@data-original-title='Remove']"}
    products_name_xpath = {"xpath": "//table[@class='table table-bordered']//td[@class='text-left']//a"}
    delivery_date_xpath = {"xpath": "//td[@class='text-left']//small"}
    out_of_stock_msg_xpath = {"xpath": "//div[contains(@class,'alert-danger')]"}
    quantity_txt_box_xpath = {"xpath": "//div[@class='input-group btn-block']//input"}
    quantity_update_button_xpath = {"xpath": "//button[@type='submit']"}
    checkout_button_link_text = {"link_text": "Checkout"}

    # methods for basic actions
    def cleanup_products_from_cart(self):
        total_prod = self.get_elements_count(self.cart_product_remove_button_xpath)
        if total_prod > 0:
            for x in range(total_prod-1, -1, -1):   # Start at total_prod-1, end at -1 (exclusive), step -1
                self.elements_click_by_index(self.cart_product_remove_button_xpath, x)

    def get_delivery_date(self):
        return self.get_elements_text_by_index(self.delivery_date_xpath, 1).split(":")[1]

    def is_product_out_of_stock_or_min_order_notified(self):
        return self.get_element_text(self.out_of_stock_msg_xpath)

    def update_product_quantity_and_check(self, new_quantity):
        self.type_into_element(new_quantity, self.quantity_txt_box_xpath)
        self.element_click(self.quantity_update_button_xpath)
        return self.get_element_attribute(self.quantity_txt_box_xpath, "value")

    def click_on_checkout(self):
        self.element_click(self.checkout_button_link_text)
        return CheckoutPage(self.driver)

    def does_product_present_in_cart(self, prod_names_list):
        # get product names from cart & store it in list cart_prod_names
        total_prod = self.get_elements_count(self.products_name_xpath)
        cart_prod_names = []
        if total_prod > 0:
            for x in range(total_prod):
                prod_name = self.get_elements_text_by_index(self.products_name_xpath, x)
                cart_prod_names.append(prod_name)

        # to compare prod_names_list with cart_prod_names
        logging.info(f"no of products added is {len(prod_names_list)} and no of cart products is {len(cart_prod_names)}")
        result = []
        for i in range(len(prod_names_list)):
            if prod_names_list[i] == cart_prod_names[i]:
                result.append(True)
            else:
                result.append(False)
        return result

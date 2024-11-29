import logging
import time

import pytest
from tests.base_test import BaseTest
from utilities import excel_utils


@pytest.mark.order(6)  # Set the desired order for this test file
class TestCheckout(BaseTest):
    @pytest.mark.parametrize("order_details", excel_utils.get_all_excel_data("payment_address"))
    def test_checkout_and_confirm_order_of_product(self, order_details, get_account):
        logging.info("test_checkout--> test_checkout_and_confirm_order_of_product started")

        products_page = self.login_and_cleanup_cart_and_back_to_products_page(get_account)
        product_specific_page = products_page.click_on_product_with_mandatory_delivery_date()  # hp_product
        product_specific_page.calender_date_picker()  # mandatory field
        product_specific_page.add_product_to_cart()
        cart_page = self.navigate_to_shopping_cart()
        checkout_page = cart_page.click_on_checkout()
        assert checkout_page.add_order_details_and_checkout(order_details).__contains__("order has been placed")

        logging.info("test_checkout--> test_checkout_and_confirm_order_of_product complted\n")

    def test_order_less_than_minimum_should_not_be_checked_out(self, get_account):
        logging.info("test_checkout--> test_order_less_than_minimum_should_not_be_checked_out started")

        products_page = self.login_and_cleanup_cart_and_back_to_products_page(get_account)
        product_specific_page = products_page.click_on_out_of_stock_minimum_order_product()
        product_specific_page.add_less_than_minimum_quantity()
        product_specific_page.add_product_to_cart()
        cart_page = self.navigate_to_shopping_cart()
        cart_page.click_on_checkout()
        assert cart_page.is_product_out_of_stock_or_min_order_notified().__contains__("Minimum order")

        logging.info("test_checkout--> test_order_less_than_minimum_should_not_be_checked_out completed\n")

    def test_out_of_stock_products_should_not_be_checked_out(self, get_account):
        logging.info("test_checkout--> test_out_of_stock_products_should_not_be_checked_out started")

        products_page = self.login_and_cleanup_cart_and_back_to_products_page(get_account)
        product_specific_page = products_page.click_on_out_of_stock_product()
        product_specific_page.add_product_to_cart()
        cart_page = self.navigate_to_shopping_cart()
        cart_page.click_on_checkout()
        assert cart_page.is_product_out_of_stock_or_min_order_notified().__contains__("not in stock")

        logging.info("test_checkout--> test_out_of_stock_products_should_not_be_checked_out completed\n")



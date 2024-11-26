import logging

import pytest
from tests.base_test import BaseTest


@pytest.mark.order(4)  # Set the desired order for this test file
class TestAddProductsToCart(BaseTest):
    def test_add_product_to_cart_from_products_page(self, get_account):
        logging.info("test_add_products_to_cart--> test_add_product_to_cart_from_products_page started")
        products_page = self.login_and_navigate_to_products_page(get_account)
        assert products_page.add_product_and_confirm_success_msg([4])  # give product position no
        logging.info("test_add_products_to_cart--> test_add_product_to_cart_from_products_page completed\n")

    def test_add_product_to_cart_without_mandatory_fields(self, get_account):
        logging.info("test_add_products_to_cart--> test_add_product_to_cart_without_mandatory_fields started")
        products_page = self.login_and_navigate_to_products_page(get_account)
        product_specific_page = products_page.click_on_product_without_mandatory_fields()
        assert product_specific_page.add_product_and_confirm_success_msg()
        logging.info("test_add_products_to_cart--> test_add_product_to_cart_without_mandatory_fields completed\n")

    def test_add_date_mandatory_product_to_cart(self, get_account):
        logging.info("test_add_products_to_cart--> test_add_date_mandatory_product_to_cart started")
        products_page = self.login_and_navigate_to_products_page(get_account)
        product_specific_page = products_page.click_on_product_with_mandatory_delivery_date()
        product_specific_page.calender_date_picker()     # mandatory field
        assert product_specific_page.add_product_and_confirm_success_msg()
        logging.info("test_add_products_to_cart--> test_add_date_mandatory_product_to_cart completed\n")

    def test_add_out_of_stock_product_to_cart(self, get_account):
        logging.info("test_add_products_to_cart--> test_add_out_of_stock_product_to_cart started")
        products_page = self.login_and_navigate_to_products_page(get_account)
        product_specific_page = products_page.click_on_out_of_stock_product()
        assert product_specific_page.add_product_and_confirm_success_msg()
        logging.info("test_add_products_to_cart--> test_add_out_of_stock_product_to_cart completed\n")

    def test_add_out_of_stock_and_minimum_order_mandatory_product_to_cart(self, get_account):
        logging.info("test_add_products_to_cart--> test_add_out_of_stock_and_minimum_order_mandatory_product_to_cart started")
        products_page = self.login_and_navigate_to_products_page(get_account)
        product_specific_page = products_page.click_on_out_of_stock_minimum_order_product()
        product_specific_page.add_product_spec()
        assert product_specific_page.add_product_and_confirm_success_msg()
        logging.info("test_add_products_to_cart--> test_add_out_of_stock_and_minimum_order_mandatory_product_to_cart completed\n")

    def test_add_product_with_less_than_minimum_order_to_cart(self, get_account):
        logging.info("test_add_products_to_cart--> test_add_product_with_less_than_minimum_order_to_cart started")
        products_page = self.login_and_navigate_to_products_page(get_account)
        product_specific_page = products_page.click_on_out_of_stock_minimum_order_product()
        product_specific_page.add_less_than_minimum_quantity()
        assert product_specific_page.add_product_and_confirm_success_msg()
        logging.info("test_add_products_to_cart--> test_add_product_with_less_than_minimum_order_to_cart completed\n")



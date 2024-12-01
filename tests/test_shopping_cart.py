import logging
import time
from datetime import datetime
import pytest
from tests.base_test import BaseTest


@pytest.mark.order(5)  # Set the desired order for this test file
class TestShoppingCart(BaseTest):
    @pytest.mark.parametrize("product_positions", [([4]), ([4, 5])])  # cases for single product & multiple products
    def test_products_added_from_product_page_in_cart(self, product_positions, get_account):
        logging.info("test_shopping_cart--> test_products_added_from_product_page_in_cart started")

        products_page = self.login_and_cleanup_cart_and_back_to_products_page(get_account)
        products_page.click_add_to_product(product_positions)   # give product position in list
        prod_names = products_page.get_product_name(product_positions)  # give product position in list
        cart_page = self.navigate_to_shopping_cart()
        prod_compare_results = cart_page.does_product_present_in_cart(prod_names)
        assert all(prod_compare_results), "One or more products are not present in the cart"

        logging.info("test_shopping_cart--> test_products_added_from_product_page_in_cart completed\n")

    def test_product_and_its_delivery_date_in_cart(self, get_account):
        logging.info("test_shopping_cart--> test_product_and_its_delivery_date_in_cart started")

        products_page = self.login_and_cleanup_cart_and_back_to_products_page(get_account)
        product_specific_page = products_page.click_on_product_with_mandatory_delivery_date()   # hp_product
        product_specific_page.calender_date_picker()  # mandatory field
        time.sleep(1)
        product_specific_page.add_product_to_cart()
        time.sleep(1)
        prod_name = [product_specific_page.get_product_name()]
        cart_page = self.navigate_to_shopping_cart()
        prod_compare_results = cart_page.does_product_present_in_cart(prod_name)
        assert all(prod_compare_results), "added product is not present in the cart"
        assert cart_page.get_delivery_date().__eq__(datetime.now().strftime("%Y-%m-%d"))

        logging.info("test_shopping_cart--> test_product_and_its_delivery_date_in_cart completed\n")

    def test_out_of_stock_notification_in_cart(self, get_account):
        logging.info("test_shopping_cart--> test_out_of_stock_notification_in_cart started")

        products_page = self.login_and_cleanup_cart_and_back_to_products_page(get_account)
        product_specific_page = products_page.click_on_out_of_stock_product()
        product_specific_page.add_product_to_cart()
        cart_page = self.navigate_to_shopping_cart()
        assert cart_page.is_product_out_of_stock_or_min_order_notified().__contains__("not in stock")

        logging.info("test_shopping_cart--> test_out_of_stock_notification_in_cart completed\n")

    def test_update_quantity_of_product_in_cart(self, get_account):
        logging.info("test_shopping_cart--> test_update_quantity_of_product_in_cart started")

        products_page = self.login_and_cleanup_cart_and_back_to_products_page(get_account)
        product_specific_page = products_page.click_on_product_without_mandatory_fields()
        product_specific_page.add_product_to_cart()
        cart_page = self.navigate_to_shopping_cart()
        assert cart_page.update_product_quantity_and_check(2).__eq__("2")   # updating & verifying with new value

        logging.info("test_shopping_cart--> test_update_quantity_of_product_in_cart completed\n")

    def test_minimum_order_notification_in_cart(self, get_account):  # adding less than intended minimum order for a product
        logging.info("test_shopping_cart--> test_minimum_order_notification_in_cart started")

        products_page = self.login_and_cleanup_cart_and_back_to_products_page(get_account)
        product_specific_page = products_page.click_on_out_of_stock_minimum_order_product()
        product_specific_page.add_less_than_minimum_quantity()
        product_specific_page.add_product_to_cart()
        cart_page = self.navigate_to_shopping_cart()
        cart_page.click_on_checkout()
        assert cart_page.is_product_out_of_stock_or_min_order_notified().__contains__("Minimum order")

        logging.info("test_shopping_cart--> test_minimum_order_notification_in_cart completed\n")










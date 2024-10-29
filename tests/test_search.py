import logging
import pytest
from pageobjects.home_page import HomePage
from tests.base_test import BaseTest


@pytest.mark.order(1)  # Set the desired order for this test file
class TestSearch(BaseTest):
    def test_search_valid_product(self):
        logging.info("test_search--> test_search_valid_product started")

        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("HP")
        assert search_page.display_status_of_valid_product()    # 2nd line name has to match with this locator

        logging.info("test_search--> test_search_valid_product completed\n")

    def test_search_invalid_product(self):
        logging.info("test_search--> test_search_invalid_product started")

        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("Honda")
        expected_txt = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_txt)

        logging.info("test_search--> test_search_invalid_product completed\n")

    def test_search_empty_product(self):
        logging.info("test_search--> test_search_empty_product started")

        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("")
        expected_txt = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_txt)

        logging.info("test_search--> test_search_empty_product completed\n")


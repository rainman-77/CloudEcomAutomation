import random
import time
from datetime import datetime
import pytest
from pageobjects.account_page import AccountPage
from pageobjects.home_page import HomePage


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:
    @staticmethod
    def generate_mail():
        cur_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + str(random.randint(1, 99))
        return f"test_ash_{cur_time}@gmail.com"

    def login_and_navigate_to_products_page(self, account):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_with_credentials(account["email"], account["password"])
        return account_page.navigate_to_product_page()

    def login_and_cleanup_cart_and_back_to_products_page(self, account):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_with_credentials(account["email"], account["password"])

        products_page = account_page.navigate_to_product_page()  # added this to avoid delay in removal if empty
        products_page.add_product_and_confirm_success_msg([4])    # give product position in list

        cart_page = account_page.click_on_shopping_cart_button()
        cart_page.cleanup_products_from_cart()
        time.sleep(1)
        return account_page.navigate_to_product_page()

    def navigate_to_shopping_cart(self):
        return AccountPage(self.driver).click_on_shopping_cart_button()

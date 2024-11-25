from pageobjects.base_page import BasePage
from pageobjects.cart_page import CartPage
from pageobjects.products_page import ProductsPage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    account_info_link_text = {"link_text": "Edit your account information"}
    desktops_catg_link_text = {"link_text": "Desktops"}
    show_all_option_link_test = {"link_text": "Show AllDesktops"}
    shopping_cart_button_xpath = {"xpath": "//span[text()='Shopping Cart']"}

    # methods for basic actions
    def is_account_info_text_displayed(self):
        return self.element_display_status(self.account_info_link_text)

    def click_on_desktops_catg(self):
        self.element_click(self.desktops_catg_link_text)

    def show_all_option(self):
        self.element_click(self.show_all_option_link_test)
        return ProductsPage(self.driver)

    def click_on_shopping_cart_button(self):
        self.element_click(self.shopping_cart_button_xpath)
        return CartPage(self.driver)

    # methods for high level actions
    def navigate_to_product_page(self):
        self.click_on_desktops_catg()
        return self.show_all_option()





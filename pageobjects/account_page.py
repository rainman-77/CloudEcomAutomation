from pageobjects.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    account_info_link_text = {"link_text": "Edit your account information"}

    def is_account_info_text_displayed(self):
        return self.element_display_status(self.account_info_link_text)



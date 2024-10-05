from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        element = None
        for loc_type, loc_value in locator.items():     # get locator dict's key-value pairs one at a time
            if "id" in loc_type:
                element = self.driver.find_element(By.ID, loc_value)
            elif "name" in loc_type:
                element = self.driver.find_element(By.NAME, loc_value)
            elif "class_name" in loc_type:
                element = self.driver.find_element(By.CLASS_NAME, loc_value)
            elif "link_text" in loc_type:
                element = self.driver.find_element(By.LINK_TEXT, loc_value)
            elif "xpath" in loc_type:
                element = self.driver.find_element(By.XPATH, loc_value)
            elif "css" in loc_type:
                element = self.driver.find_element(By.CSS_SELECTOR, loc_value)
        return element

    def type_into_element(self, text, locator):
        element = self.get_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator):
        element = self.get_element(locator)
        element.click()

    def element_display_status(self, locator):
        element = self.get_element(locator)
        return element.is_displayed()

    def get_element_text(self, locator):
        element = self.get_element(locator)
        return element.text





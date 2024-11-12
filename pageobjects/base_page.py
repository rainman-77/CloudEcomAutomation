import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    default_timeout = 15

    def wait_for_condition(self, locator, condition):
        wait = WebDriverWait(self.driver, self.default_timeout)
        for loc_type, loc_value in locator.items():
            if loc_type == "id":
                return wait.until(condition((By.ID, loc_value)))
            elif loc_type == "name":
                return wait.until(condition((By.NAME, loc_value)))
            elif loc_type == "class_name":
                return wait.until(condition((By.CLASS_NAME, loc_value)))
            elif loc_type == "link_text":
                return wait.until(condition((By.LINK_TEXT, loc_value)))
            elif loc_type == "xpath":
                return wait.until(condition((By.XPATH, loc_value)))
            elif loc_type == "css":
                return wait.until(condition((By.CSS_SELECTOR, loc_value)))

    def explicit_wait(self, locator):
        return self.wait_for_condition(locator, ec.visibility_of_element_located)

    def explicit_wait_for_elements(self, locator):
        return self.wait_for_condition(locator, ec.presence_of_all_elements_located)

    def get_element(self, locator):         # to get web element without waiting like for hidden locators
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

    def get_elements(self, locator):
        elements = []
        for loc_type, loc_value in locator.items():
            if "id" in loc_type:
                elements = self.driver.find_elements(By.ID, loc_value)
            elif "name" in loc_type:
                elements = self.driver.find_elements(By.NAME, loc_value)
            elif "class_name" in loc_type:
                elements = self.driver.find_elements(By.CLASS_NAME, loc_value)
            elif "link_text" in loc_type:
                elements = self.driver.find_elements(By.LINK_TEXT, loc_value)
            elif "xpath" in loc_type:
                elements = self.driver.find_elements(By.XPATH, loc_value)
            elif "css" in loc_type:
                elements = self.driver.find_elements(By.CSS_SELECTOR, loc_value)
        return elements

    def type_into_element(self, text, locator):
        element = self.explicit_wait(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def type_into_elements(self, text, locator, index=0):
        self.explicit_wait_for_elements(locator)
        elements = self.get_elements(locator)
        if elements and index < len(elements):
            elements[index].click()
            elements[index].clear()
            elements[index].send_keys(text)
        else:
            raise IndexError(f"No element found at index {index}")

    def element_click(self, locator):
        element = self.explicit_wait(locator)
        element.click()

    def elements_click_by_index(self, locator, index=0):
        # self.explicit_wait_for_elements(locator)
        elements = self.get_elements(locator)
        if elements and index < len(elements):
            elements[index].click()
        else:
            raise IndexError(f"No element found at index {index}")

    def element_display_status(self, locator):
        element = self.explicit_wait(locator)
        return element.is_displayed()

    def elements_display_status_by_index(self, locator, index=0):
        self.explicit_wait_for_elements(locator)
        elements = self.get_elements(locator)
        if elements and index < len(elements):
            return elements[index].is_displayed()
        else:
            raise IndexError(f"No element found at index {index}")

    def get_element_text(self, locator):
        element = self.explicit_wait(locator)
        return element.text

    def get_elements_text_by_index(self, locator, index=0):
        self.explicit_wait_for_elements(locator)
        elements = self.get_elements(locator)
        if elements and index < len(elements):
            return elements[index].text
        else:
            raise IndexError(f"No element found at index {index}")

    def get_element_attribute(self, locator, attribute_name):
        element = self.explicit_wait(locator)
        return element.get_dom_attribute(attribute_name)

    def get_elements_count(self, locator):
        try:
            self.explicit_wait_for_elements(locator)
            elements = self.get_elements(locator)
            return len(elements)
        except Exception as e:
            logging.error(f"Unable to retrieve elements count for locator: {locator}. Exception: {e}")
            return 0  # Return 0 if no elements are found or another issue occurs

    def select_dropdown_option_by_index(self, locator, index):
        element = self.explicit_wait(locator)
        select = Select(element)
        select.select_by_index(index)

    def select_dropdown_option_by_text(self, locator, text):
        element = self.explicit_wait(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def upload_file_using_hidden_locator(self, locator, file_path):
        abs_file_path = os.path.abspath(file_path)
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, abs_file_path)






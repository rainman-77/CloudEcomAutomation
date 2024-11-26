import logging
import time
from datetime import datetime
from pageobjects.base_page import BasePage


class ProductSpecificPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    add_to_cart_button_id = {"id": "button-cart"}
    product_added_success_msg_xpath = {"xpath": "//div[contains(text(), 'Success: You have added ')]"}
    radio_button_xpath = {"xpath": "//div[@id='input-option218']//input"}
    check_boxes_xpath = {"xpath": "//div[@class='checkbox']//input"}
    text_box_id = {"id": "input-option208"}
    select_drop_down_id = {"id": "input-option217"}
    text_area_id = {"id": "input-option209"}
    upload_file_button_id = {"id": "input-option222"}   # hidden file upload locator
    calender_button_xpath = {"xpath": "//div[@class='input-group datetime']//button"}
    calender_time_picker_button_xpath = {"xpath": "//li[@class='picker-switch accordion-toggle']"}
    minimum_quantity_msg_xpath = {"xpath": "//div[@class='alert alert-info']"}
    quantity_txt_box_id = {"id": "input-quantity"}
    product_name_xpath = {"xpath": "//div[@id='content']//div//h1"}

    calender_date_button_xpath = {"xpath": "//div[@class='input-group date']//button"}
    cal_picker_switch_xpath = {"xpath": "//th[@class='picker-switch']"}
    cal_get_year_button_xpath = {"xpath": "//div[@class='datepicker-months']//th[@class='picker-switch']"}
    cal_year_next_button_xpath = {"xpath": "//div[@class='datepicker-months']//th[@class='next']"}
    cal_month_selection_elements_xpath = {"xpath": "//div[@class='datepicker-months']//span"}
    cal_current_day_button_xpath = {"xpath": "//div[@class='datepicker-days']//td[@class='day today']"}

    calender_time_button_xpath = {"xpath": "//div[@class='input-group time']//button"}
    cal_hr_display_elements_xpath = {"xpath": "//span[@data-action='showHours']"}
    cal_min_display_elements_xpath = {"xpath": "//span[@data-action='showMinutes']"}
    hr_up_button_elements_xpath = {"xpath": "//a[@data-action='incrementHours']"}
    hr_down_button_elements_xpath = {"xpath": "//a[@data-action='decrementHours']"}
    min_up_button_elements_xpath = {"xpath": "//a[@data-action='incrementMinutes']"}
    min_down_button_elements_xpath = {"xpath": "//a[@data-action='decrementMinutes']"}

    # methods for basic actions
    def add_product_to_cart(self):
        self.element_click(self.add_to_cart_button_id)

    def get_product_name(self):
        return self.get_element_text(self.product_name_xpath)

    def is_product_added_success_msg_displayed(self):
        return self.element_display_status(self.product_added_success_msg_xpath)

    @staticmethod
    def get_current_date_and_time():
        cur_date_time = datetime.now().strftime("%Y %m %H %M").split(' ')
        cur_year = int(cur_date_time[0])
        cur_month = int(cur_date_time[1])
        cur_hr = cur_date_time[2]
        cur_min = cur_date_time[3]
        return cur_year, cur_month, cur_hr, cur_min

    def calender_date_picker(self):
        self.element_click(self.calender_date_button_xpath)
        cur_year, cur_month, *_ = ProductSpecificPage.get_current_date_and_time()
        self.element_click(self.cal_picker_switch_xpath)
        cal_year = int(self.get_element_text(self.cal_get_year_button_xpath))
        while cal_year != cur_year:
            self.element_click(self.cal_year_next_button_xpath)     # until year matches click next
            cal_year += 1
        self.elements_click_by_index(self.cal_month_selection_elements_xpath, cur_month-1)
        self.element_click(self.cal_current_day_button_xpath)

    def calender_time_picker(self):
        _, _, cur_hr, cur_min = ProductSpecificPage.get_current_date_and_time()
        cal_hr = 0
        cal_min = 0
        while cal_min != cur_min:
            self.elements_click_by_index(self.min_up_button_elements_xpath, 1)
            cal_min = self.get_elements_text_by_index(self.cal_min_display_elements_xpath, 1)
        while cal_hr != cur_hr:
            self.elements_click_by_index(self.hr_up_button_elements_xpath, 1)
            cal_hr = self.get_elements_text_by_index(self.cal_hr_display_elements_xpath, 1)

    def calender_date_time_picker(self):
        cur_year, cur_month, *_ = ProductSpecificPage.get_current_date_and_time()   # date_picker
        self.elements_click_by_index(self.cal_picker_switch_xpath, 3)
        cal_year = int(self.get_elements_text_by_index(self.cal_get_year_button_xpath, 1))
        while cal_year != cur_year:
            self.elements_click_by_index(self.cal_year_next_button_xpath, 1)     # until year matches click next
            cal_year += 1
        self.elements_click_by_index(self.cal_month_selection_elements_xpath, cur_month + 11)
        time.sleep(1)
        self.element_click(self.cal_current_day_button_xpath)

        self.element_click(self.calender_time_picker_button_xpath)    # change to time view

        _, _, cur_hr, cur_min = ProductSpecificPage.get_current_date_and_time()     # time_picker
        cal_hr = 0
        cal_min = 0
        while cal_min != cur_min:
            self.elements_click_by_index(self.min_up_button_elements_xpath, 0)
            cal_min = self.get_elements_text_by_index(self.cal_min_display_elements_xpath, 0)
        while cal_hr != cur_hr:
            self.elements_click_by_index(self.hr_up_button_elements_xpath, 0)
            cal_hr = self.get_elements_text_by_index(self.cal_hr_display_elements_xpath, 0)

    def add_product_spec(self):
        self.element_click(self.radio_button_xpath)
        self.elements_click_by_index(self.check_boxes_xpath, 1)
        self.type_into_element("adding product spec", self.text_box_id)
        self.select_dropdown_option_by_index(self.select_drop_down_id, 1)
        self.type_into_element("testing text area", self.text_area_id)
        self.upload_file_using_hidden_locator(self.upload_file_button_id, "testdata/dummy_file_for_upload.txt")
        self.calender_date_picker()
        time.sleep(1)
        self.element_click(self.calender_time_button_xpath)
        self.calender_time_picker()
        self.element_click(self.calender_time_button_xpath)
        time.sleep(1)
        self.element_click(self.calender_button_xpath)
        self.calender_date_time_picker()
        self.element_click(self.calender_button_xpath)

    def add_less_than_minimum_quantity(self):
        less_quantity = int(self.get_element_text(self.minimum_quantity_msg_xpath).split()[-1]) - 1
        self.add_product_spec()
        self.type_into_element(less_quantity, self.quantity_txt_box_id)

    # methods for high level actions
    def add_product_and_confirm_success_msg(self):
        self.add_product_to_cart()
        return self.is_product_added_success_msg_displayed()

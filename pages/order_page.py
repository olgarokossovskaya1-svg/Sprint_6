from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def wait_for_order_form_to_load(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.NAME_INPUT)
    
    def fill_name(self, name):
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
    
    def fill_surname(self, surname):
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, surname)
    
    def fill_address(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)
    
    def select_metro_station(self):
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.wait_for_element_to_be_visible(OrderPageLocators.FIRST_METRO_STATION)
        self.click_element(OrderPageLocators.FIRST_METRO_STATION)
    
    def fill_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
    
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)
    
    def fill_first_page(self, name, surname, address, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.select_metro_station()
        self.fill_phone(phone)
        self.click_next_button()
    
    def select_date(self):
        self.click_element(OrderPageLocators.DATE_INPUT)
        self.wait_for_element_to_be_visible(OrderPageLocators.TODAY_DATE)
        self.click_element(OrderPageLocators.TODAY_DATE)
    
    def select_rental_period(self):
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.wait_for_element_to_be_visible(OrderPageLocators.PERIOD_DAY)
        self.click_element(OrderPageLocators.PERIOD_DAY)
    
    def select_black_color(self):
        self.click_element(OrderPageLocators.BLACK_COLOR)
    
    def fill_comment(self, comment):
        if comment:
            self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)
    
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
    
    def fill_second_page(self, comment=""):
        self.select_date()
        self.select_rental_period()
        self.select_black_color()
        self.fill_comment(comment)
        self.click_order_button()
    
    def confirm_order(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.CONFIRM_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)
    
    def is_order_success_displayed(self):
        return self.is_element_displayed(OrderPageLocators.SUCCESS_MODAL, timeout=10)
import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config import BASE_URL


class MainPage(BasePage):
    def open(self):
        with allure.step("Открыть главную страницу"):
            self.open_url(BASE_URL)
            self.wait_for_element_to_be_visible(MainPageLocators.TOP_ORDER_BUTTON)
    
    def accept_cookies(self):
         with allure.step("Принять cookies, если отображаются"):
            if self.is_element_displayed(MainPageLocators.COOKIE_BUTTON):
                self.click_element(MainPageLocators.COOKIE_BUTTON)
    
    def click_question(self, index):
        with allure.step(f"Кликнуть по вопросу №{index}"):
            question_locator = MainPageLocators.question_locator(index)
            self.scroll_to_element(question_locator)
            self.click_element_with_js(question_locator)
    
    def get_question_text(self, index):
        question_locator = MainPageLocators.question_locator(index)
        return self.get_element_text(question_locator)
    
    def get_answer_text(self, index):
        with allure.step(f"Получить текст ответа для вопроса №{index}"):
            answer_locator = MainPageLocators.answer_locator(index)
            self.wait_for_element_to_be_visible(answer_locator, timeout=5)
            return self.get_element_text(answer_locator)
    
    def is_answer_displayed(self, index):
        return self.is_element_displayed(MainPageLocators.answer_locator(index), timeout=5)
    
    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)
    
    def click_bottom_order_button(self):
        self.scroll_to_bottom()
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
    
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
    
    def is_on_main_page(self):
        current_url = self.get_current_url()
        return BASE_URL == current_url
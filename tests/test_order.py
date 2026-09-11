import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.yandex_page import YandexPage
from data.test_data import ORDER_DATA_1, ORDER_DATA_2
import config


class TestOrder:

    @allure.title("Заказ через верхнюю кнопку с первым набором данных")
    def test_order_top_button_first_dataset(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form_to_load()
        order_page.fill_first_page(
            ORDER_DATA_1["name"],
            ORDER_DATA_1["surname"],
            ORDER_DATA_1["address"],
            ORDER_DATA_1["phone"]
        )
        order_page.fill_second_page(ORDER_DATA_1["comment"])
        order_page.confirm_order()
        assert order_page.is_order_success_displayed()


    def test_order_top_button_second_dataset(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form_to_load()
        order_page.fill_first_page(
            ORDER_DATA_2["name"],
            ORDER_DATA_2["surname"],
            ORDER_DATA_2["address"],
            ORDER_DATA_2["phone"]
        )
        order_page.fill_second_page(ORDER_DATA_2["comment"])
        order_page.confirm_order()
        assert order_page.is_order_success_displayed()


    def test_order_bottom_button_first_dataset(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form_to_load()
        order_page.fill_first_page(
            ORDER_DATA_1["name"],
            ORDER_DATA_1["surname"],
            ORDER_DATA_1["address"],
            ORDER_DATA_1["phone"]
        )
        order_page.fill_second_page(ORDER_DATA_1["comment"])
        order_page.confirm_order()
        assert order_page.is_order_success_displayed()


    def test_order_bottom_button_second_dataset(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form_to_load()
        order_page.fill_first_page(
            ORDER_DATA_2["name"],
            ORDER_DATA_2["surname"],
            ORDER_DATA_2["address"],
            ORDER_DATA_2["phone"]
        )
        order_page.fill_second_page(ORDER_DATA_2["comment"])
        order_page.confirm_order()
        assert order_page.is_order_success_displayed()


class TestNavigation:

    @allure.title("Переход на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == config.BASE_URL


    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        main_window = main_page.get_current_window_handle()
        main_page.click_yandex_logo()
        main_page.wait_for_new_window([main_window])

        new_window = main_page.get_window_handles()[-1]
        main_page.switch_to_window(new_window)

        yandex_page = YandexPage(driver)

        assert yandex_page.wait_until_dzen_page_loaded()

        yandex_page.close_current_window()
        main_page.switch_to_window(main_window)
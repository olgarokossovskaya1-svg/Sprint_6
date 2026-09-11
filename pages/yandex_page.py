from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from config import DZEN_URL


class YandexPage(BasePage):
    def wait_until_dzen_page_loaded(self):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(DZEN_URL))
from .base_page import BasePage
from config import DZEN_URL


class YandexPage(BasePage):
    def is_on_dzen_page(self):
        return self.get_current_url() == DZEN_URL
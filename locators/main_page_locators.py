class MainPageLocators:
    COOKIE_BUTTON = ("id", "rcc-confirm-button")
    TOP_ORDER_BUTTON = ("xpath", "//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = ("xpath", "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = ("xpath", "//a[@href='/']")
    YANDEX_LOGO = ("xpath", "//a[@href='//yandex.ru']")
    
    @staticmethod
    def question_locator(index):
        return ("id", f"accordion__heading-{index}")
    
    @staticmethod
    def answer_locator(index):
        return ("id", f"accordion__panel-{index}")
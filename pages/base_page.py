from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def open_url(self, url):
        self.driver.get(url)
    
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
    
    def click_element_with_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_element_text(self, locator):
        return self.find_element(locator).text
    
    def is_element_displayed(self, locator, timeout=3):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except TimeoutException:
            return False
    
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_new_window(self, current_windows, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > len(current_windows)
        )
    
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    def get_window_handles(self):
        return self.driver.window_handles
    
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
    
    def close_current_window(self):
        self.driver.close()
    
    def get_current_url(self):
        return self.driver.current_url
    
    def get_page_title(self):
        return self.driver.title
    
    def refresh_page(self):
        self.driver.refresh()
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def wait_for_url_change(self, original_url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != original_url
        )
    
    def wait_for_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: text in d.current_url
        )
    
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
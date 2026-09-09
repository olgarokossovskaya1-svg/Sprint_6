import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    service = Service()
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
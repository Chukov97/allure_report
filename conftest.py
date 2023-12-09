import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture()
def open_browser():
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.driver.set_window_size(width=1920, height=1080)

    yield

    browser.quit()

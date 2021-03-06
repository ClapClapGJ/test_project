import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
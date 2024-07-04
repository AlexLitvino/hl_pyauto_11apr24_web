import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

from web_tests.helpers.user import User
from web_tests.pages.login_page import LoginPage

# TODO: specify path to chromedriver here
driver_path = r''


@pytest.fixture()
def driver():
    driver = Chrome(service=Service(driver_path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def valid_user():
    return User('standard_user', 'secret_sauce')


@pytest.fixture(scope='session')
def locked_out_user():
    return User('locked_out_user', 'secret_sauce')


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver).navigate()

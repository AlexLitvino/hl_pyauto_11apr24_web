import datetime
import os

import pytest
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from web_tests.helpers.project_helpers import get_browser, get_screenshot_directory, create_screenshots_directory
from web_tests.helpers.user import User
from web_tests.pages.login_page import LoginPage


@pytest.fixture()
def driver():
    browser = get_browser()
    if browser == 'chrome':
        driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError('Browser not supported')
    driver.maximize_window()
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


@pytest.fixture(scope='session', autouse=True)
def create_screenshot_directory():
    create_screenshots_directory()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    import pdb; pdb.set_trace()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        driver = item.funcargs["login_page"].driver

        file_name = f"{item.name}_{datetime.datetime.now().strftime('%Y_%m_%d-%H_%M')}.png"
        file_path = os.path.join(get_screenshot_directory(), file_name)
        driver.save_screenshot(file_path)

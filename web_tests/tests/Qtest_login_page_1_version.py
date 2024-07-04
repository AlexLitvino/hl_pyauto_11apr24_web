"""First iteration of tests"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pytest

# TODO: specify path to chromedriver here
driver_path = r''


@pytest.mark.skip(reason='Not implemented yet')
@pytest.mark.layout
def test_login_page_layout():
    raise NotImplementedError


def test_successful_login():
    """
    1. Navigate to base url
    2. Enter 'standard_user' as username
    3. Enter 'secret_sauce' as password
    4. Click Login button.
    Verify that Inventory page is displayed
    """
    driver = Chrome(service=Service(driver_path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://www.saucedemo.com/')
    time.sleep(1)
    valid_user = 'standard_user'
    valid_password = 'secret_sauce'

    username_input_field = driver.find_element(By.ID, 'user-name')
    password_input_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_input_field.send_keys(valid_user)
    password_input_field.send_keys(valid_password)
    time.sleep(1)
    login_button.click()
    time.sleep(1)
    inventory_container = driver.find_element(By.ID, 'inventory_container')
    assert inventory_container.is_displayed(), "Inventory pag is not displayed"

    driver.quit()


def test_locked_out_login():
    """
    1. Navigate to base url
    2. Enter 'locked_out_user' as username
    3. Enter 'secret_sauce' as password
    4. Click Login button.
    Verify that Login page is still displayed
    Verify that "Epic sadface: Sorry, this user has been locked out." is displayed
    Verify that error marker is displayed for username text field
    Verify that error marker is displayed for password text field
    """
    driver = Chrome(service=Service(driver_path))
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get('https://www.saucedemo.com/')

    valid_user = 'locked_out_user'
    valid_password = 'secret_sauce'

    username_input_field = driver.find_element(By.ID, 'user-name')
    password_input_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_input_field.send_keys(valid_user)
    password_input_field.send_keys(valid_password)
    login_button.click()

    assert login_button.is_displayed(), "Login page is not displayed"

    error_message = driver.find_element(By.TAG_NAME, 'h3')
    assert error_message.is_displayed(), "Error message is not displayed"
    assert error_message.text == 'Epic sadface: Sorry, this user has been locked out.', \
        f"It is expected 'Epic sadface: Sorry, this user has been locked out.' is displayed but '{error_message.text}' is displayed"

    username_error_marker = driver.find_element(By.XPATH, "//input[@id='user-name']/following-sibling::*[local-name()='svg']")
    password_error_marker = driver.find_element(By.XPATH, "//input[@id='password']/following-sibling::*[local-name()='svg']")

    assert username_error_marker.is_displayed(), "Error marker for username text field is not displayed"
    assert password_error_marker.is_displayed(), "Error marker for password text field is not displayed"

    driver.quit()


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_username():
    raise NotImplementedError


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_password():
    raise NotImplementedError


def test_navigation_between_inventory_page_and_inventory_item_page():
    """
    1. Navigate to base url
    2. Enter 'standard_user' as username
    3. Enter 'secret_sauce' as password
    4. Click Login button.
    Verify that Inventory page is displayed
    # OR: Navigate to Inventory page as standard user
    5. Select first item on Inventory page.
    Verify that page for the first item is displayed.
    6. Click Back button.
    Verify that Inventory page is displayed
    """
    driver = Chrome(service=Service(driver_path))
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get('https://www.saucedemo.com/')

    valid_user = 'standard_user'
    valid_password = 'secret_sauce'

    username_input_field = driver.find_element(By.ID, 'user-name')
    password_input_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_input_field.send_keys(valid_user)
    password_input_field.send_keys(valid_password)
    login_button.click()

    inventory_container = driver.find_element(By.ID, 'inventory_container')
    assert inventory_container.is_displayed(), "Inventory page is not displayed"

    item_1 = driver.find_elements(By.XPATH, "//div[contains(@class, 'inventory_item_name')]")[0]
    item_1.click()

    # on item#1 page
    back_button = driver.find_element(By.ID, 'back-to-products')
    assert back_button.is_displayed(), "Item page is not displayed"

    back_button.click()

    inventory_container = driver.find_element(By.ID, 'inventory_container')
    assert inventory_container.is_displayed(), "Inventory page is not displayed"

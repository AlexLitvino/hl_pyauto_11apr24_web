"""First iteration of tests"""

from selenium.webdriver.common.by import By

import pytest

from web_tests.helpers.resources import Resource

# TODO: specify path to chromedriver here
driver_path = r'/home/olytvynov/Projects/HL/drivers/chromedriver-linux64-126.0.6478.126/chromedriver'


@pytest.mark.skip(reason='Not implemented yet')
@pytest.mark.layout
def test_login_page_layout():
    raise NotImplementedError


def test_successful_login(login_page, valid_user):
    """
    1. Navigate to base url
    2. Enter 'standard_user' as username
    3. Enter 'secret_sauce' as password
    4. Click Login button.
    Verify that Inventory page is displayed
    """
    inventory_page = login_page.perform_successful_login(valid_user)
    assert inventory_page.is_displayed(), "Inventory pag is not displayed"


def test_locked_out_login(login_page, locked_out_user):
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
    login_page.perform_unsuccessful_login(locked_out_user)

    assert login_page.is_displayed(), "Login page is not displayed"

    assert login_page.error_message.is_displayed(), "Error message is not displayed"
    observed_error_message_text = login_page.get_error_message()
    assert observed_error_message_text == Resource.LoginPage.LOCKED_OUT_USERR_ERROR_MESSAGE, \
        f"It is expected 'Epic sadface: Sorry, this user has been locked out.' is displayed but '{observed_error_message_text}' is displayed"

    assert login_page.username_error_marker.is_displayed(), "Error marker for username text field is not displayed"
    assert login_page.password_error_marker.is_displayed(), "Error marker for password text field is not displayed"


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_username():
    raise NotImplementedError


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_password():
    raise NotImplementedError


@pytest.mark.skip(reason="Temporary skipped")
def test_navigation_between_inventory_page_and_inventory_item_page(driver):
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

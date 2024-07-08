"""First iteration of tests"""

import pytest

from web_tests.helpers.resources import Resource


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
    assert observed_error_message_text == Resource.LoginPage.LOCKED_OUT_USERR_ERROR_MESSAGE + 'Q', \
        f"It is expected 'Epic sadface: Sorry, this user has been locked out.' is displayed but '{observed_error_message_text}' is displayed"

    assert login_page.username_error_marker.is_displayed(), "Error marker for username text field is not displayed"
    assert login_page.password_error_marker.is_displayed(), "Error marker for password text field is not displayed"


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_username():
    raise NotImplementedError


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_password():
    raise NotImplementedError


def test_navigation_between_inventory_page_and_inventory_item_page(login_page, valid_user):
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
    inventory_page = login_page.perform_successful_login(valid_user)

    assert inventory_page.is_displayed(), "Inventory page is not displayed"

    inventory_item_page = inventory_page.navigate_to_item(1)

    # on item#1 page
    assert inventory_item_page.back_button.is_displayed(), "Item page is not displayed"

    inventory_page = inventory_item_page.back()
    assert inventory_page.is_displayed(), "Inventory page is not displayed"

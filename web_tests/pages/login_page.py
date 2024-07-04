from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage
from web_tests.pages.inventory_page import InventoryPage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    USERNAME_INPUT_FIELD = (By.ID, 'user-name')
    PASSWORD_INPUT_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.TAG_NAME, 'h3')
    USERNAME_ERROR_MARKER = (By.XPATH, "//input[@id='user-name']/following-sibling::*[local-name()='svg']")
    PASSWORD_ERROR_MARKER = (By.XPATH, "//input[@id='password']/following-sibling::*[local-name()='svg']")

    @property
    def username_input_field(self):
        return self.get_element(LoginPage.USERNAME_INPUT_FIELD)

    @property
    def password_input_field(self):
        return self.get_element(LoginPage.PASSWORD_INPUT_FIELD)

    @property
    def login_button(self):
        return self.get_element(LoginPage.LOGIN_BUTTON)

    @property
    def error_message(self):
        return self.get_element(LoginPage.ERROR_MESSAGE)

    @property
    def username_error_marker(self):
        return self.get_element(LoginPage.USERNAME_ERROR_MARKER)

    @property
    def password_error_marker(self):
        return self.get_element(LoginPage.PASSWORD_ERROR_MARKER)

    def navigate(self):
        self.driver.get('https://www.saucedemo.com/')
        return self

    def is_displayed(self):
        return self.login_button.is_displayed()

    def enter_username(self, user):
        self.username_input_field.send_keys(user.username)
        return self

    def enter_password(self, user):
        self.password_input_field.send_keys(user.password)
        return self

    def click_login_button(self):
        self.login_button.click()

    def fill_credentials_and_click_login_button(self, user):
        self.enter_username(user)
        self.enter_password(user)
        self.click_login_button()

    def perform_successful_login(self, user):
        self.fill_credentials_and_click_login_button(user)
        return InventoryPage(self.driver)

    def perform_unsuccessful_login(self, user):
        self.fill_credentials_and_click_login_button(user)
        return self

    def get_error_message(self):
        return self.error_message.text

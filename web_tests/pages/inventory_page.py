from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    INVENTORY_CONTAINER = (By.ID, 'inventory_container')

    @property
    def inventory_container(self):
        return self.get_element(InventoryPage.INVENTORY_CONTAINER)

    def is_displayed(self):
        return self.inventory_container.is_displayed()

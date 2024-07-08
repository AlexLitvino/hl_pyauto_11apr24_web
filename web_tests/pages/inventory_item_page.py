from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage
#from web_tests.pages.inventory_page import InventoryPage
import web_tests.pages.inventory_page as inventory_page


class InventoryItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    BACK_BUTTON = (By.XPATH, '//button[@id="back-to-products"]')

    @property
    def back_button(self):
        return self.get_element(InventoryItemPage.BACK_BUTTON)

    def back(self):
        self.back_button.click()
        return inventory_page.InventoryPage(self.driver)

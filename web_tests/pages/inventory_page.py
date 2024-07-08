from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage
#from web_tests.pages.inventory_item_page import InventoryItemPage
import web_tests.pages.inventory_item_page as inventory_item_page


class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    INVENTORY_CONTAINER = (By.ID, 'inventory_container')
    ITEM = (By.XPATH, '//div[@class="inventory_list"]/div[{number}]/div[@class="inventory_item_description"]//a')

    @property
    def inventory_container(self):
        return self.get_element(InventoryPage.INVENTORY_CONTAINER)

    @property
    def item_link(self):
        def get_item(number):
            return self.get_element(InventoryPage.ITEM, number=number)
        return get_item

    def is_displayed(self):
        return self.inventory_container.is_displayed()

    def navigate_to_item(self, number):
        self.item_link(number).click()
        return inventory_item_page.InventoryItemPage(self.driver)


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, timeout=3, **kwargs):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((locator[0], locator[1].format(**kwargs))))


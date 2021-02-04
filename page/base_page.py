import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _driver: WebDriver = None
    _black_list = [(MobileBy.ID, "iv_close")]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            locator1 = (locator, value)
            WebDriverWait(self._driver, 2).until(expected_conditions.element_to_be_clickable(locator1))
            return element
        except Exception:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(locator, value)

    def steps(self, path):
        with open(path) as f:
            _steps = yaml.safe_load(f)
        for _step in _steps:
            if "by" in _step.keys():
                _element = self.find(_step["by"], _step["locator"])
            if "action" in _step.keys():
                _action = _step["action"]
                if _action == "click":
                    _element.click()
                if _action == "send_keys":
                    _element.send_keys(_step["value"])

        return self

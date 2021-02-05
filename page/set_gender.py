from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage

import page.add_contact


class Set_Gender(BasePage):

    def set_gender(self, _gender):
        if _gender == "male":
            locator = (MobileBy.XPATH, "//*[@text='男']")
        elif _gender == "female":
            locator = (MobileBy.XPATH, "//*[@text='女']")

        ele = WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()

        return page.add_contact.Add_Contact(self._driver)
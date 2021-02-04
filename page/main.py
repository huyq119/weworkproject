from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contacts import Contacts


class Main(BasePage):

    def goto_contacts(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text = '通讯录']").click()
        return Contacts(self._driver)

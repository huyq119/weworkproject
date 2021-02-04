from appium.webdriver.common.mobileby import MobileBy

import page.add_contact_option
from page.base_page import BasePage
from page.set_department import Set_Department
import page.message_contact_fail


class Add_Contact(BasePage):

    def add_contact(self, _name, _phone):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ern']"
                                  "//*[@resource-id='com.tencent.wework:id/b78']").send_keys(_name)
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/f5y']"
                                  "//*[@resource-id = 'com.tencent.wework:id/fuy']").send_keys(_phone)
        self.goto_set_department().set_department()
        self.find(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        return page.add_contact_option.Add_Contact_Option(self._driver)

    def add_contact_fail(self, _name, _phone):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ern']"
                                  "//*[@resource-id='com.tencent.wework:id/b78']").send_keys(_name)
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/f5y']"
                                  "//*[@resource-id = 'com.tencent.wework:id/fuy']").send_keys(_phone)
        self.goto_set_department().set_department()
        self.find(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        return page.message_contact_fail.Message_Contact_Fail(self._driver)

    def goto_set_department(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/er0']"
                                  "//*[@resource-id='com.tencent.wework:id/b81']").click()
        return Set_Department(self._driver)

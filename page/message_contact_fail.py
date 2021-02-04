from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
import page.add_contact


class Message_Contact_Fail(BasePage):

    def message_contact_fail_confirm(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/bom").click()
        return page.add_contact.Add_Contact(self._driver)

    def get_message_text(self):
        message_text = self.find(MobileBy.ID, "com.tencent.wework:id/boj").text
        return message_text

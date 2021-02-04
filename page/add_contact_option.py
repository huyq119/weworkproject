from appium.webdriver.common.mobileby import MobileBy

from page.add_contact import Add_Contact
from page.base_page import BasePage
import page.contacts

class Add_Contact_Option(BasePage):

    def goto_add_contact(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/csn").click()
        return Add_Contact(self._driver)

    def goto_contacts_new(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/idp").click()
        return page.contacts.Contacts(self._driver)

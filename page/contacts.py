from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.add_contact_option import Add_Contact_Option
from page.base_page import BasePage


class Contacts(BasePage):

    def goto_add_contact_option(self):
        """
        滑动查找元素
        :return:
        """
        self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                  'new UiScrollable(new UiSelector().'
                                  'scrollable(true).instance(0)).'
                                  'scrollIntoView(new UiSelector().'
                                  'text("添加成员").instance(0));').click()
        return Add_Contact_Option(self._driver)

    def get_name_list(self):
        sleep(5)
        element_list = self._driver.find_elements(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/em4']"
                                                                  "//*[@class='android.widget.TextView']")
        name_list = []
        for element in element_list:
            name_list.append(element.text)
        return name_list

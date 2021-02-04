from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Set_Department(BasePage):

    def set_department(self):
        return self.find(MobileBy.ID, "com.tencent.wework:id/gzz").click()

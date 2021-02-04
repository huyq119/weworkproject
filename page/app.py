from time import sleep

import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.tencent.wework"
    _activity = ".launch.LaunchSplashActivity"

    def start(self):
        if self._driver is None:
            caps = {'platformName': 'Android', 'platformVersion': '6.0.1',
                    'deviceName': yaml.safe_load(open("../page/configuration.yml"))["caps"]["deviceName"],
                    'appPackage': self._package, 'appActivity': self._activity,
                    'noReset': 'true', 'unicodeKeyBoard': 'true', 'resetKeyBoard': 'true',
                    'ensureWebviewsHavePages': True}
            # 初始化driver
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package, self._activity)

        self._driver.implicitly_wait(3)
        return self

    def main(self) -> Main:
        return Main(self._driver)

    def quit(self):
        sleep(3)
        self._driver.quit()

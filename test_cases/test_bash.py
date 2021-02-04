from page.app import App

# 封装app启动和退出

class TestBase():

    def setup(self):
        self.app = App()

    def teardown(self):
        self.app.quit()
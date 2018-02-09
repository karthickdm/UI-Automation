import logging
import os
import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Environment(object):

    def __init__(self):

        hkex_test_data = open(os.path.expanduser('~/.TOUCHSRC')).read()
        test_data = json.loads(hkex_test_data)
        print (test_data)

        if "base_url" in test_data:
            self.base_url = test_data["base_url"]

        if "username" in test_data:
            self.username = test_data["username"]

        if "password" in test_data:
            p = test_data["password"]
            self.password = self._password(p)

        if "browser" in test_data:
            self.browser = test_data["browser"]

        if "width" in test_data:
            self.width = test_data["width"]

        if "height" in test_data:
            self.height = test_data["height"]

    def create_browser_instance(self):
        if self.browser == "chrome":
            self.chrome_browser()
        elif self.browser == "IE":
            logging.info("Trying to locate the IE driver")
            self.driver = webdriver.Chrome("$HOME//AppData//Local//Programs//Python//Python35//Scripts//chromedriver.exe")
            logging.info("Instanciate IE Driver")
        return self.driver

    def chrome_browser(self):
        home = os.path.expanduser("~")
        driver_path = home + "\\AppData\\Local\Programs\\Python\\Python35\\Scripts\\"
        self.driver = webdriver.Chrome(driver_path+"//chromedriver.exe")
        self.option = Options()
        self.option.add_argument("'disable-infobars'")
        self.set_browser_windows_size()
        self.set_default_implicit_wait_time()

    def set_default_implicit_wait_time(self):
        self.driver.implicitly_wait(40)

    def set_browser_windows_size(self):
        self.driver.set_window_size(width=self.width, height=self.height)

    def navigate_to_home(self):
        self.driver.get(self.base_url)

    def _password(self, p):
        p_value = str(p)
        before_slice = base64.b64decode(p_value)
        password = str(before_slice).replace("'", "").lstrip("b")
        return password

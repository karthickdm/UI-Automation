from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    userName = (By.CSS_SELECTOR, 'form > input:nth-child(2)')
    passWord = (By.CSS_SELECTOR, "form > input:nth-child(4)")
    signIn = (By.CSS_SELECTOR, "form > input:nth-child(5)")
    profile = (By.CSS_SELECTOR, "div > button > img")
    sing_out = (By.CSS_SELECTOR, "div > ul:nth-child(2) > li:nth-child(4) > ul > li")

    def enter_username(self, uname):
        enter_username = self.find_element(*self.userName)
        enter_username.send_keys(uname)

    def enter_password(self, password):
        enter_password = self.find_element(*self.passWord)
        enter_password.send_keys(password)

    def click_sign_in(self):
        self.find_element(*self.signIn).click()

    def click_profile_page(self):
        self.find_element(*self.profile).click()

    def click_sign_out(self):
        self.find_element(*self.sing_out).click()
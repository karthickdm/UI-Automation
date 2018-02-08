import unittest
import xmlrunner
from Environment.Environment import Environment
from Pages import LoginPage, HomePage


class TrialTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        envi = Environment()
        cls.driver = envi.create_browser_instance()
        envi.navigate_to_home()
        cls.username = envi.username
        cls.password = envi.password

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        loginPage = LoginPage.LoginPage(self.driver)
        loginPage.enter_username(self.username)
        loginPage.enter_password(self.password)
        loginPage.click_sign_in()

    def tearDown(self):
        loginPage = LoginPage.LoginPage(self.driver)
        loginPage.click_profile_page()
        loginPage.click_sign_out()

    def test_epam(self):
        homepage = HomePage.HomePage(self.driver)
        homepage.click_jobs()
        homepage.enter_search("software testing")

    def test_epam1(self):
        homepage = HomePage.HomePage(self.driver)
        homepage.click_jobs()
        homepage.enter_search("software testing")

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))


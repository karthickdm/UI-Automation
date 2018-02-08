class BasePage(object):

    def __init__(self, selenium_driver):
        self.driver = selenium_driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def find_element_by_css_selector(self, loc):
        return self.driver.find_element_by_css_selector(loc)
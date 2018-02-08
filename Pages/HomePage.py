from Pages.BasePage import BasePage

class HomePage(BasePage):

    #Locators
    JOBS = "ul > li:nth-child(3)"
    SEARCH = "div:nth-child(1) > artdeco-typeahead > artdeco-typeahead-input > input:nth-child(2)"

    def click_jobs(self):
        self.find_element_by_css_selector(self.JOBS).click()

    def enter_search(self, value):
        enter_search = self.find_element_by_css_selector(self.SEARCH)
        enter_search.send_keys(value)

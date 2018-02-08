from Pages.BasePage import BasePage

class HomePage(BasePage):

    #Locators
    Jobs = "ul > li:nth-child(3)"

    selectors = {
        "Jobs": "ul > li:nth-child(3)",
        "search": "div:nth-child(1) > artdeco-typeahead > artdeco-typeahead-input > input:nth-child(2)"
    }

    def click_jobs(self):
        self.find_element_by_css_selector(self.Jobs).click()

    def enter_search(self, value):
        enter_search = self.find_element_by_css_selector(self.selectors["search"])
        enter_search.send_keys(value)
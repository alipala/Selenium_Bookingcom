from Locators.locators import Locators

class GooglePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_textbox_xpath = Locators.search_textbox_xpath
        self.search_button_name = Locators.search_button_name
        self.search_result_item_xpath = Locators.search_result_item_xpath

    def search_google(self):
        self.driver.find_element_by_xpath(self.search_textbox_xpath).send_keys("booking.com")
        self.driver.find_element_by_name(self.search_button_name).submit()
        self.driver.find_element_by_xpath(self.search_result_item_xpath).click()


    def is_title_matches(self):
        return "Booking.com" in self.driver.title







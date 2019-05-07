from Locators.locators import Locators

class BookingHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.destination_input_id = Locators.destination_input_id
        self.autocomplete_item_xpath = Locators.autocomplete_item_xpath
        self.date_field_name = Locators.date_field_name

    def search_hotel(self):
        self.driver.find_element_by_id(self.destination_input_id).clear()
        self.driver.find_element_by_id(self.destination_input_id).send_keys("Amsterdam")
        self.driver.find_element_by_xpath(self.autocomplete_item_xpath).click()
        self.driver.find_element_by_name(self.date_field_name).click()

class Locators:
    '''
    These are the page locators
    '''

    # Google page locators
    search_textbox_xpath = "//input[@name='q']"
    search_button_name = "btnK"
    search_result_item_xpath = "//h3[@class='LC20lb'][contains(.,'Booking.com: 28,422,184 hotel and property listings worldwide. 177+ ...')]"

    # Booking.com Home page locators
    destination_input_id = "ss"
    autocomplete_item_xpath = "(//span[contains(.,'Amsterdam, Noord-Holland, Netherlands')])[1]"
    date_field_name = "xp__dates-inner"
    # Search Result page locators
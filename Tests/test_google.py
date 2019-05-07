import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.google_page import GooglePage
from Pages.booking_home_page import BookingHomePage
from Base.base import Base

class TestGoogle(Base):

    def test_01_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        google_page = GooglePage(driver)
        google_page.search_google()
        assert google_page.is_title_matches()

    # def test_02_search_hotel(self):
    #     driver = self.driver
    #     booking_home = BookingHomePage(driver)
    #     booking_home.search_hotel()


if __name__ == "__main__":
    unittest.main()


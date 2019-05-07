import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Base.base import Base
from Pages.booking_home_page import BookingHomePage

class TestBookingHome(Base):

    def test_01_search_hotel(self):
        driver = self.driver
        booking_home = BookingHomePage()
        booking_home.search_hotel()

if __name__ == "__main__":
    unittest.main()


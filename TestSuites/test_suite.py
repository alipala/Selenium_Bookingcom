import unittest
from Tests.test_google import TestGoogle
from Tests.test_booking_home import TestBookingHome
import HtmlTestRunner

# get all tests from Test classess
google_test = unittest.TestLoader().loadTestsFromTestCase(TestGoogle)
booking_home_test = unittest.TestLoader().loadTestsFromTestCase(TestBookingHome)

# create a test suite to execute tests
test_suite = unittest.TestSuite([google_test])



runner = HtmlTestRunner.HTMLTestRunner(output="D:/Selenium_Bookingcom/Reports")
runner.run(test_suite)


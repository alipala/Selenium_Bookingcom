import unittest
from selenium import webdriver

class Base(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Selenium_Bookingcom/Drivers/chromedriver.exe")
        print("-----------------------------------------")
        print("Test started")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        if cls.driver != None:
            print("-----------------------------------------")
            print("Tests finished")
            cls.driver.close()
            cls.driver.quit()
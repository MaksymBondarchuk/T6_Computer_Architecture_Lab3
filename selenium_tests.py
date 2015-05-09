__author__ = 'andreynikolin'

import unittest
from selenium import webdriver
from selenium import *
import os
import time


class TestLab(unittest.TestCase):

    def setUp(self):
        os.environ["SELENIUM_SERVER_JAR"] = "/Users/andreynikolin/PycharmProjects/selenium-server-standalone-2.45.0.jar"
        self.driver = webdriver.Safari()

    def test_create_read(self):
        driver = self.driver
        driver.get("http://localhost:8080")
        self.assertIn("Lab3::HomePage", driver.title)
        # elem = driver.find_element_by_name("q")
        time.sleep(5)
        driver.find_element_by_id("nameAdd").send_keys("Lab NN")
        driver.find_element_by_id("aboutAdd").send_keys("About NN")
        driver.find_element_by_id("stateAdd").send_keys("State NN")
        driver.find_element_by_id("buttonAdd").click()
        time.sleep(5)
        body = driver.find_element_by_tag_name("body")
        checktext = body.text
        assert "Lab NN" in checktext

    def test_update(self):
        driver = self.driver
        driver.get("http://localhost:8080")

        driver.find_element_by_id("inputUpdate").send_keys("Lab NNN")
        driver.find_element_by_id("updateButton").click()
        time.sleep(2)
        driver.get("http://localhost:8080")
        body = driver.find_element_by_tag_name("body")
        checktext = body.text
        assert "Lab NNN" in checktext


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
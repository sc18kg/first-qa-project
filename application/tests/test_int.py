import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db 
from application.models import Film, Review

# Set test variables for test admin user
test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('DATABASE_URI'))
        app.config['SECRET_KEY'] = getenv('SECRET_KEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/kieron/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestAddfilm(TestBase):

    def test_addfilm(self):

        # Click add film menu link
        self.driver.find_element_by_xpath("<xpath for Register button in nav bar>").click()
        time.sleep(1)

        # Fill in the form for adding a film
        self.driver.find_element_by_xpath('<xpath for film title>').send_keys('The Incredibles')
        self.driver.find_element_by_xpath('<xpath for description>').send_keys(
            'Super hero family who fight crime')
        self.driver.find_element_by_xpath('<xpath for released_at>').send_keys(
            '2006')
        self.driver.find_element_by_xpath('<xpath for age rating>').send_keys(
            'U')
        self.driver.find_element_by_xpath('<xpath for add film button>').click()
        time.sleep(1)

        # Assert that browser redirects to film list page
        assert url_for('filmlist') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)
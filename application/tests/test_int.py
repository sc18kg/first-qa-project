from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db 
from application.models import Film, Review

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
        app.config['SECRET_KEY'] = getenv('SECRET_KEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        db.create_all()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:5000")


    def tearDown(self):
        self.driver.quit()
        db.drop_all()
    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)


class TestAddfilm(TestBase):

    def test_addfilm(self):

        # Click add film menu link
        self.driver.find_element_by_xpath("/html/body/a[3]").click()


        # Fill in the form for adding a film
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys('The Incredibles')
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys(
            'Super hero family who fight crime')
        self.driver.find_element_by_xpath('//*[@id="released_at"]').send_keys(
            '2006')
        self.driver.find_element_by_xpath('//*[@id="age_rating"]').send_keys(
            'U')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()


        # Assert that browser redirects to film list page
        assert url_for('home') in self.driver.current_url




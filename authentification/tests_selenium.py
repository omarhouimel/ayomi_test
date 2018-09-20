import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumTests(LiveServerTestCase):

    def setUp(self):
        get_user_model().objects.create_user(username="admin", email="test@gmail.com", password="admin",
                                             first_name="test prenom", last_name="test nom")
        geckodriver_path = os.path.join(settings.BASE_DIR, 'geckodriver')
        # you have to copy geckodriver in your /usr/local/bin if you are using Linux

        self.selenium = webdriver.Firefox()
        super(SeleniumTests, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SeleniumTests, self).tearDown()

    def test_sing_up(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')
        #find the form element
        first_name = selenium.find_element_by_id('first_name')
        last_name = selenium.find_element_by_id('last_name')

        email = selenium.find_element_by_id('email')
        password = selenium.find_element_by_id('password')


        submit = selenium.find_element_by_name('register')

        #Fill the form with data
        first_name.send_keys('ayomi')
        last_name.send_keys('ayomi')

        email.send_keys('ayomi@gamil.com')
        password.send_keys('ayomi')


        #submitting the form
        submit.send_keys(Keys.RETURN)

    def test_update_mail(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/details')
        email = selenium.find_element_by_name('email')
        submit = selenium.find_element_by_name('register')
        email.send_keys('ayomiapp@gamil.com')
        submit.send_keys(Keys.RETURN)


    def test_login(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/details')
        email = selenium.find_element_by_id('login_name')
        password = selenium.find_element_by_id('login_password')
        submit = selenium.find_element_by_name('register_login')
        # You Must put the email and password of a user saved in the database
        email.send_keys('houimelomar@gmail.com')
        password.send_keys('0')
        submit.send_keys(Keys.RETURN)




from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.serializers import json
from django.test import TestCase
from django.test.client import Client


# Create your tests here.
from django.urls import reverse


class UserTestCase(TestCase):
    def setUp(self):
        # Create User
        get_user_model().objects.create_user(username="admin", email="test@gmail.com", password="admin",
                                 first_name="test prenom", last_name="test nom")
        self.client = Client()


    def test_login_user(self):
        login = self.client.login(username='admin', password='admin')
        self.assertTrue(login)


    def test_index_page_access(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


    def test_details_page_without_access(self):
            response = self.client.post(reverse('details'))
            self.assertRedirects(response, '/')



    def test_email_updated_with_success(self):

        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('details'), {'email': 'new@gmail.com'})
        user = User.objects.get(username='new@gmail.com')    # because the user_name is user eamil
        self.assertEqual('new@gmail.com',  user.email )






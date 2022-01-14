from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.test import APIClient


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')

        self.user_data = {
            'email': 'email@gmail.com',
            'username': 'email',
            'password': 'email@gmail.com'
        }

        self.client = APIClient()

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

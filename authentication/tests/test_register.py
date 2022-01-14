from .test_setup import TestSetUp
from django.contrib.auth import get_user_model
from rest_framework import status


class TestViews(TestSetUp):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(res.status_code, 201)

    def test_user_using_email(self):
        res = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(res.data['email'], self.user_data['email'])

    def test_user_using_username(self):
        res = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(res.data['username'], self.user_data['username'])

    def test_password_being_hashed(self):
        payload = {
            'email': 'test@coding.com',
            'username': 'welldone123',
            'password': 'Test_name',
        }
        res = self.client.post(self.register_url, payload)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_registeration_without_username(self):
        """test creating user that already exists"""
        payload = {
            'email': 'test@coding.com',
            'password': 'Test_name',
        }
        res = self.client.post(self.register_url, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """test that the password is more than 5 characters"""
        payload = {
            'email': 'test@coding.com',
            'password': 'we',
            'name': 'Test',
        }
        res = self.client.post(self.register_url, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

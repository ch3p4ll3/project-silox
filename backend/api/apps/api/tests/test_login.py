from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AccountTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.token = Token.objects.create(user=self.user)

    def test_login_no_data(self):
        """
        Test login with no data
        """
        url = reverse('auth_login')
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_invalid_account(self):
        """
        Test login with invalid account
        """
        url = reverse('auth_login')
        data = {'username': 'test', 'password': 'test'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_valid_account(self):
        """
        Test login with valid account
        """
        url = reverse('auth_login')
        data = {'username': 'username', 'password': 'password'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['token'], self.token.key)

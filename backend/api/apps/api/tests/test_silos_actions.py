from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Silos
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AccountTests(APITestCase):
    def setUp(self):
        self.silos = Silos.objects.create(name='name', status=True)
        self.user = User.objects.create_user(username='username', password='password')
        self.token = Token.objects.create(user=self.user)

    def test_invalid_silos(self):
        """
        Test invalid silos
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get('http://localhost:8000/silos/2/', format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_silos(self):
        """
        Test valid silos
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get('http://localhost:8000/silos/1/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], self.silos.status)
        self.assertEqual(response.data['name'], self.silos.name)

    def test_valid_silos_list(self):
        """
        Test valid silos list
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get('http://localhost:8000/silos/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['status'], self.silos.status)
        self.assertEqual(response.data[0]['name'], self.silos.name)

    def test_silos_fill(self):
        """
        Test silos fill
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get('http://localhost:8000/silos/1/actions/fill/100/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_silos_empty(self):
        """
        Test silos fill
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get('http://localhost:8000/silos/1/actions/empty/100/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_silos_idle(self):
        """
        Test silos fill
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get('http://localhost:8000/silos/1/actions/idle/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

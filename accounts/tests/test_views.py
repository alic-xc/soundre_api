from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class AccountViewTestCase(APITestCase):
    """ """

    def setUp(self):
        self.client = APIClient()
        self.users = [
            {
                'first_name': 'john',
                'last_name': 'doe',
                'email': 'dummy@example.com',
                'username': 'dummy@example',
                'password': 'abcd123456'
            },
            {
                'first_name': 'sam',
                'last_name': 'kelvin',
                'email': 'dummy2@example.com',
                'username': 'dummy2@example',
                'password': 'abcd123456',
            }
        ]

    def test_account_get_unauthenticated(self):
        """ """
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_account_create_users(self):
        """ """
        for data in self.users:
            response = self.client.post('/account/', data, 'json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_account_incorrect_data_or_empty_data(self):
        """ Testing incorrect data on post request to /account/ view """

        data_1 = {
            'first_name': 'john',
            'last_name': 'doe',
            'email': 'dummy@example.com',
            'username': '',
            'password': 'abcd123456'
        }
        data_2 = {
            'first_name': 'sam',
            'last_name': 'kelvin',
            'email': '',
            'username': 'dummy',
            'password': 'abcd123456',
        }

        response = self.client.post('/account/', data_1, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post('/account/', data_2, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_duplicate_username(self):
        """ Testing for duplicate username. Expected to return False """

        data_1 = {
            'first_name': 'john',
            'last_name': 'doe',
            'email': 'dummy@example.com',
            'username': 'dummy',
            'password': 'abcd123456'
        }
        data_2 = {
            'first_name': 'sam',
            'last_name': 'kelvin',
            'email': 'dummy2@example.com',
            'username': 'dummy',
            'password': 'abcd123456',
        }

        response = self.client.post('/account/', data_1, 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('/account/', data_2, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_duplicate_email(self):
        """ Testing for duplicate email. Expected to return False """

        data_1 = {
            'first_name': 'john',
            'last_name': 'doe',
            'email': 'dummy@example.com',
            'username': 'dummy',
            'password': 'abcd123456'
        }
        data_2 = {
            'first_name': 'sam',
            'last_name': 'kelvin',
            'email': 'dummy@example.com',
            'username': 'dummy2',
            'password': 'abcd123456',
        }

        response = self.client.post('/account/', data_1, 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('/account/', data_2, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_login(self):
        login_details = [
            {
                'username': self.users[0]['username'],
                'password': self.users[0]['password'],
            },
            {
                'username': self.users[1]['username'],
                'password': self.users[1]['password'],
            }
        ]

        #creating new users
        for data in self.users:
            response = self.client.post('/account/', data, 'json')

        for details in login_details:
            response = self.client.post('/api/login', details, 'json')
            self.assertIn('refresh', response.data)
            self.assertIn('access', response.data)

    def test_account_invalid_login(self):
        """ """

        invalid_login_details = [
            {'username': 'test01', 'password': 'BxdsD2133'},
            {'username': 'test02', 'password': 'BxdsD2133'},
        ]

        for details in invalid_login_details:
            response = self.client.post('/api/login', details, 'json')
            self.assertNotIn('response', response.data)
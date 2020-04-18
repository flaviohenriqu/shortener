from django.test import Client, TestCase
from django.urls import reverse


class UserLoginTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        # create user
        self.client.post(
            reverse('users:create'),
            {
                "username": "john",
                "email": "user@test.com",
                "password": "smith",
                "confirm_password": "smith",
                "date_joined": "2020-04-17T00:00"
            }
        )

    def test_login_sucessful(self):
        response = self.client.post(reverse('users:token_obtain_pair'), {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'access')

    def test_login_fail(self):
        response = self.client.post(reverse('users:token_obtain_pair'), {'username': 'john', 'password': 'smith1'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content, b'{"detail":"No active account found with the given credentials"}')

    def test_refresh_token(self):
        response = self.client.post(reverse('users:token_obtain_pair'), {'username': 'john', 'password': 'smith'})
        refresh_token = response.json()['refresh']
        token = response.json()['access']
        refresh_response = self.client.post(
            reverse('users:token_refresh'),
            {'refresh': f'{refresh_token}'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(refresh_response.json()['access'], token)

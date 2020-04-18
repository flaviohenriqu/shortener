from rest_framework.test import APIClient, APITestCase

from django.http import HttpResponseRedirect
from django.urls import reverse


class URLShortenerTest(APITestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = APIClient()
        # create user
        response = self.client.post(
            reverse('users:create'),
            {
                "username": "john",
                "email": "user@test.com",
                "password": "smith",
                "confirm_password": "smith",
                "date_joined": "2020-04-17T00:00"
            }
        )
        self.token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_url_short_invalid(self):
        response = self.client.post(reverse('core:list'), {'full_url': 'google.com'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'full_url': ['Enter a valid URL.']})

    def test_url_short_successful(self):
        response = self.client.post(reverse('core:list'), {'full_url': 'https://www.google.com'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['full_url'], 'https://www.google.com')

    def test_redirect_short_url(self):
        response = self.client.post(reverse('core:list'), {'full_url': 'https://www.google.com'})
        self.assertEqual(response.status_code, 201)
        slug = response.json()['slug']

        response_redirect = self.client.get(reverse('core:redirect', kwargs={'slug': f'{slug}'}))
        self.assertEqual(response_redirect.status_code, 302)
        self.assertEqual(type(response_redirect), HttpResponseRedirect)

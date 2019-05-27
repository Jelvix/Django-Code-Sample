from rest_framework.test import APITestCase
from django.test import Client
from django.urls import reverse
from rest_framework import status

from accounts.models import User
from accounts.tests.factory import UserModelFactory


class UserViewTest(APITestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        url = reverse('register')

        self.response_get = self.client.get(url)
        self.csrf_token = self.client.cookies['csrftoken'].value
        self.data = {"email": "ut@mail.com",
                     "password": "123pASS",
                     "csrfmiddlewaretoken": self.csrf_token
                     }

        self.response = self.client.post(url, self.data)
        self.user = UserModelFactory()
        self.user_to_delete = UserModelFactory()

    def test_user_registration(self):
        self.assertEqual(self.response.status_code, status.HTTP_302_FOUND)
        self.assertIsNotNone(User.objects.get(email=self.data["email"]))

    def test_user_accounts_get(self):
        self.client.login(email=self.user.email, password='1234')
        url = reverse('user-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_accounts_post(self):
        self.client.login(email=self.user.email, password='1234')
        url = reverse('user-list')
        data = {"email": "ut2@mail.com",
                "password": "123pASS",
                "csrfmiddlewaretoken": self.csrf_token
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_accounts_details(self):
        self.client.login(email=self.user.email, password='1234')
        url = reverse('user-detail', args=([self.user.pk]))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_accounts_details_put(self):
        self.client.login(email=self.user.email, password="123ASS")
        url = reverse('user-detail', args=([self.user.pk]))
        data = {"email": "ut2@mail.com",
                "password": "123pASS",
                "csrfmiddlewaretoken": self.csrf_token
                }
        response = self.client.put(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_accounts_details_patch(self):
        self.client.login(email=self.user.email, password="123ASS")
        url = reverse('user-detail', args=([self.user.pk]))
        data = {"email": "ut2@mail.com",
                "password": "1pASS",
                "csrfmiddlewaretoken": self.csrf_token
                }
        response = self.client.put(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_accounts_details_patch(self):
        self.client.login(email=self.user.email, password="123ASS")
        url = reverse('user-detail', args=([self.user_to_delete.pk]))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.serializers import UserSerializer
from accounts.tests.factory import UserModelFactory


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user = UserModelFactory()
        self.data = {
            'email': self.user.email,
            'password': self.user.password,
        }

    def test_password_validation(self):
        data = {
            'email': 'qwe@qwe.coom',
            'password': 'qewqeqeqeqw'
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        user = get_user_model().objects.get(email=data['email'])
        self.assertEqual(serializer.data['password'], user.password)

from django.test import TestCase

from accounts.models import User


class UserManagerTest(TestCase):
    def test_crete_user(self):
        self.assertTrue(User.objects.create_user('e12@eee.ee', 'password'))
        with self.assertRaisesRegexp(ValueError, '^The given email must be set$'):
            User.objects.create_user(email=None, password='password')

    def test_create_super_user(self):
        u = User.objects.create_superuser('e12@eee.ee', 'password')
        self.assertTrue(u.is_superuser)
        with self.assertRaisesRegexp(ValueError, '^Superuser must have is_superuser=True.$'):
            User.objects.create_superuser('e12@eee.ee', 'password', is_superuser=False)

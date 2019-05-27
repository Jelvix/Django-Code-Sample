from django.test import TestCase

from accounts.models import User
from accounts.tests import factory


class UserModelTests(TestCase):
    """
    class with users' model unit tests
    """

    def setUp(self):
        self.u = factory.UserModelFactory(first_name="Jane", last_name="Doe")
        self.us = factory.UserModelFactory(first_name="Jane")
        self.ad = factory.UserModelFactory(is_staff=True)

    def test_user_model(self):
        """
        Test user.__str__ with full name, first name and email.
        test if user an be staff
        :return:
        """
        check = str(self.u.first_name) + ' ' + str(self.u.last_name)
        self.assertEqual(self.u.__str__(), check, msg="Something wrong with user __str__ method with full name")

        check = str(self.us.get_short_name())
        self.assertEqual(self.us.__str__(), check, msg="Something wrong for user.__str__ with first name")

        self.assertTrue(self.ad.is_staff, msg="Wrong is_staff field")
        self.assertEqual(self.ad.__str__(), self.ad.email, msg="Something wrong with __str__ for email")

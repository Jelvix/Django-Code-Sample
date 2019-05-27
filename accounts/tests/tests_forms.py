from django.test import TestCase
from accounts.forms import RegisterForm
from accounts.tests import factory


class UserFormTest(TestCase):
    def setUp(self):
        self.u = factory.UserModelFactory(first_name="Jane", last_name="Doe")

    def test_UserForm_valid(self):
        form = RegisterForm(
            data={'email': "mail@ff.ff", 'password': self.u.password, 'first_name': self.u.first_name, 'last_name': self.u.last_name,
                  'avatar': self.u.avatar})
        self.assertTrue(form.is_valid())

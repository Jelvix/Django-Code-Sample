import factory

from accounts.models import User


class UserModelFactory(factory.django.DjangoModelFactory):

    """Create a user Factory with just email and passsword"""

    class Meta:
        model = User

    email = factory.Sequence(lambda n: 'ut{0}@test.net'.format(n))
    password = factory.PostGenerationMethodCall('set_password', '1234')
    avatar = factory.django.ImageField(color='blue')

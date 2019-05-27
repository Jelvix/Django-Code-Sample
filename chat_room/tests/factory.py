import factory
from django.conf import settings

from accounts.tests.factory import UserModelFactory
from chat_room.models import Room, Message


class RoomModelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Room

    title = factory.Sequence(lambda n: "Some{0}".format(n))


class MessageModelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Message

    text = "test"
    room = factory.SubFactory(RoomModelFactory)
    sender = factory.SubFactory(UserModelFactory)
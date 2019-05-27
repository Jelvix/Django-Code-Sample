from django.test import TestCase

from chat_room.models import Message, Room
from chat_room.serializers import RoomSerializer, MessageSerializer
from chat_room.tests.factory import RoomModelFactory, UserModelFactory


class RoomSerializerTest(TestCase):

    def test_room_serial(self):
        data = {
            'title': 'qwe',
            'staff_only': False,
            'room_messages': None

        }
        serializer = RoomSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        room = serializer.save()
        self.assertIsInstance(room, Room)


class MessageSerializerTest(TestCase):
    def test_message(self):
        room = RoomModelFactory()
        user = UserModelFactory()
        data = {
            'text': 'some text',
            'room': room.id,
            'sender': user.id
        }
        serializer = MessageSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        mess = serializer.save()
        self.assertIsInstance(mess, Message)

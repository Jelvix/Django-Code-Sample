from django.test import TestCase
from chat_room.tests import factory


class RoomModelTests(TestCase):

    def test_room_model(self):
        room = factory.RoomModelFactory()
        self.assertTrue(len(room.title) < 255, msg="Wrong length of title")
        title = room.title
        self.assertEqual(room.__str__(), title, msg="Wrong __str__")
        room_admin = factory.RoomModelFactory(staff_only=True)
        self.assertTrue(room_admin)

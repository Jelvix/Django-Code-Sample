from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.factory import UserModelFactory
from chat_room.models import Room, Message
from chat_room.tests.factory import RoomModelFactory, MessageModelFactory


class RoomViewTest(APITestCase):
    def setUp(self):
        self.user = UserModelFactory()
        self.client.login(email=self.user.email, password='1234')
        self.room = RoomModelFactory()
        self.messages = MessageModelFactory(room=self.room)
        self.messages2 = MessageModelFactory(room=self.room)
        self.messages3 = MessageModelFactory(room=self.room)

    def test_chat_room_list(self):
        self.client = Client(enforce_csrf_checks=True)
        url = reverse('register')
        self.response_get = self.client.get(url)
        self.client.login(email=self.user.email, password='1234')
        self.csrf_token = self.client.cookies['csrftoken'].value

        url = reverse('chat_list')
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

    def test_chat_room_details(self):
        self.client = Client(enforce_csrf_checks=True)
        url = reverse('register')
        self.response_get = self.client.get(url)
        self.client.login(email=self.user.email, password='1234')
        self.csrf_token = self.client.cookies['csrftoken'].value

        url = reverse('room_details', args=([self.room.pk]))
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

    def test_chat_room_get(self):
        """
        Test endpoint that get the list of rooms.
        :return: unit tests result about status and context of response
        """
        url = reverse('room-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = Room.objects.all()
        for each in titles:
            self.assertContains(response, each)

    def test_chat_room_post(self):
        url = reverse('room-list')
        data = {"title": "test", }
        response = self.client.post(url, data, format='json')
        new = Room.objects.get(title="test")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(new, Room)

    def test_chat_room_get_one(self):
        url = reverse('room-detail', args=([self.room.pk]))
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.room.title)

    def test_chat_room_put(self):
        url = reverse('room-detail', args=([self.room.pk]))
        data = {"title": "testput", }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Room.objects.get(title="testput"))

    def test_chat_room_patch(self):
        url = reverse('room-detail', args=([self.room.pk]))
        data = {"title": "testpatch", }
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Room.objects.get(title="testpatch"))

    def test_chat_room_delete(self):
        url = reverse('room-detail', args=([self.room.pk]))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_messages_get(self):
        url = reverse('message-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = []
        for each in Message.objects.all():
            n_data = {
                "room": each.room_id,
                "sender": each.sender_id,
                "text": each.text,
            }
            data.append(n_data)
        self.assertJSONEqual(response.content.decode('UTF-8'), data)

    def test_messages_post(self):
        url = reverse('message-list')
        data = {
            "text": "bla,bla,bla",
            "room": self.room.id,
            "sender": self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(Message.objects.filter(text=data["text"], room=data["room"], sender=data["sender"]))

    def test_messages_get_one(self):
        url = reverse('message-detail', args=([self.messages.pk]))
        response = self.client.get(url, format='json')
        data = {
            "room": self.messages.room_id,
            "sender": self.messages.sender_id,
            "text": self.messages.text,
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content.decode('UTF-8'), data)

    def test_messages_put(self):
        url = reverse('message-detail', args=([self.messages.pk]))
        data = {
            "room": self.messages.room_id,
            "sender": self.messages.sender_id,
            "text": "put",
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Message.objects.get(text="put"))

    def test_message_patch(self):
        url = reverse('message-detail', args=([self.messages.pk]))
        data = {
            "room": self.messages.room_id,
            "sender": self.messages.sender_id,
            "text": "patch",
        }
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Message.objects.get(text="patch"))

    def test_message_delete(self):
        url = reverse('message-detail', args=([self.messages.pk]))
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

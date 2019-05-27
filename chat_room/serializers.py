from rest_framework import serializers
from .models import Message, Room


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text', 'room', 'sender')


class RoomSerializer(serializers.ModelSerializer):
    room_messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('title', 'staff_only', 'room_messages', )

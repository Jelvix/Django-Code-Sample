from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, DeleteView
from rest_framework import viewsets

from chat_room.models import Room, Message
from chat_room.serializers import RoomSerializer, MessageSerializer


class ChatRoomList(LoginRequiredMixin, ListView):
    model = Room
    template_name = "chat/chat_list.html"


class ChatRoomDetails(LoginRequiredMixin, DetailView):
    model = Room
    template_name = "chat/chat_details.html"


class ChatRoomViewSet(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

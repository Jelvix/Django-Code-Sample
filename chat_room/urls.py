from rest_framework import routers
from django.conf.urls import url

from .views import (ChatRoomList, ChatRoomDetails, ChatRoomViewSet, MessageViewSet)

router = routers.DefaultRouter()
router.register(r'chat_rooms', ChatRoomViewSet)
router.register(r'chat_messages', MessageViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^list/', ChatRoomList.as_view(), name='chat_list'),
    url(r'^room/(?P<pk>\d+)/',  ChatRoomDetails.as_view(), name='room_details'),
]

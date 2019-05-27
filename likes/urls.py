from django.conf.urls import url
from rest_framework import routers

from likes.views import LikesCreateView, LikeViewSet

router = routers.DefaultRouter()
router.register(r'likes', LikeViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^like/(?P<type>\d+)/(?P<id>\d+)/', LikesCreateView.as_view(), name='like'),
]

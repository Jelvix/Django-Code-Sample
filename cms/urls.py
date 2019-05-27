from django.urls import include
from rest_framework import routers

from cms import views
from django.conf.urls import url


router = routers.DefaultRouter()

router.register(r'posts', views.TournamentPostViewSet)
router.register(r'tournaments', views.TournamentViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^tags_input/', include('tags_input.urls', namespace='tags_input')),

    url(r'^tournament/list/', views.TournamentListView.as_view(), name='tournament_list'),
    url(r'^tournament/detail/(?P<id>\d+)/', views.TournamentDetailView.as_view(), name='tournament_detail'),

    url(r'^tournament/event/list/', views.EventListView.as_view(), name='event'),
    url(r'^tournament/event/(?P<id>\d+)/detail/', views.EventDetailView.as_view(), name='event_detail'),

    url(r'^tournament/post/(?P<pk>\d+)/edit', views.PostEditionView.as_view(), name='edit_post'),
    url(r'^tournament/post/(?P<post_id>\d+)/', views.TournamentPostDetailView.as_view(), name='posts_detail'),
    url(r'^tournament/comment/(?P<post_id>\d+)/edition/', views.CommentUpdateView.as_view(), name='comment_edition'),
    url(r'^tournament/comment/(?P<post_id>\d+)/delete/', views.CommentDeleteView.as_view(), name='delete_post_comment'),
    url(r'^tournament/comment/(?P<post_id>\d+)/', views.TournamentPostCommentCreateView.as_view(), name='post_comment'),
    url(r'^tournament/create_post/', views.TournamentPostCreateView.as_view(), name='crete_post'),


    url(r'^tournament/post_list/', views.TournamentPostListView.as_view(), name='post_list')
    ]

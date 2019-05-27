from rest_framework import routers
from django.conf.urls import url
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)
from rest_framework_swagger.views import get_swagger_view

from .views import UserViewSet, RegisterUserView


router = routers.DefaultRouter()
router.register(r'accounts', UserViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^registration/', RegisterUserView.as_view(), name='register'),
    url(r'^login/', LoginView.as_view(), name='login'),

    url(r'^reset_password/', PasswordResetView.as_view(), name='reset_password_form'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^logout/', LogoutView.as_view(), name='logout'),
]

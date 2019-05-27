"""testcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework_swagger.views import get_swagger_view

from cms import views

schema_view = get_swagger_view(title='CMS API')


urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^tags_input/', include('tags_input.urls', namespace='tags_input')),

    url(r'^docs/', schema_view),

    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('accounts.urls')),

    url(r'^chat/', include('chat_room.urls')),

    url(r'^likes/', include('likes.urls')),

    url(r'^tournaments/', include('cms.urls')),
    url(r'^', views.TournamentPostListView.as_view()),
]


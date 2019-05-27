from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from rest_framework import viewsets

from likes.models import Like
from django.http import JsonResponse
# from django.urls import reverse_lazy
from likes.serializers import LikeSerializer


class LikesCreateView(LoginRequiredMixin, CreateView):
    model = Like

    def get(self, request, *args, **kwargs):
        query = {
            'content_type_id': self.kwargs['type'],
            'object_id': self.kwargs['id'],
            'user_id': self.request.user.id
        }
        like, is_created = self.model.objects.get_or_create(**query)
        if not is_created:
            like.delete()
        return JsonResponse({'status': 'ok', 'counter': self.model.objects.filter(content_type_id=self.kwargs['type'],
                                                                                  object_id=self.kwargs['id']).count()})


class LikeViewSet(viewsets.ModelViewSet):

    serializer_class = LikeSerializer
    queryset = Like.objects.all()


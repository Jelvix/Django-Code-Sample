from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django_filters import rest_framework as filters
from django_filters.views import FilterView
from rest_framework import viewsets

from cms.filter import PostFilter
from cms.forms import CommentForm, PostForm
from cms.models import Comment, Tournament, TournamentPost, Game, Event
from cms.serializers import CommentSerializer, TournamentSerializer, TournamentPostSerializer, GameSerializer


class ActiveUrlMixin:
    active_url = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'active_url': self.get_active_url()})
        return context

    def get_active_url(self):
        if self.active_url is None:
            raise ValueError('Not implemented')
        return self.active_url


class TournamentPostListView(ActiveUrlMixin, FilterView):
    queryset = TournamentPost.objects.filter(is_publish=True)
    template_name = "tournament_post_list.html"
    active_url = 'post'
    filterset_class = PostFilter

    def get_queryset(self):
        return self.queryset.annotate(comments_count=Count('tournament_post'), likes_count=Count('likes'))


class TournamentPostDetailView(DetailView):
    model = TournamentPost
    template_name = "post_detail.html"
    pk_url_kwarg = 'post_id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'form': CommentForm, 'comments': self.object.tournament_post.all()[:5]})
        return context


class TournamentPostCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "tournament_post_form.html"
    form_class = CommentForm

    def form_valid(self, form):
        form = form.save(commit=False)
        form.tournament_post = TournamentPost.objects.get(id=self.kwargs['post_id'])
        form.author = self.request.user
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('posts_detail', kwargs={'post_id': self.kwargs['post_id']})


class TournamentPostCreateView(ActiveUrlMixin, LoginRequiredMixin, CreateView):
    model = TournamentPost
    template_name = "tournament_post_form.html"
    active_url = 'create_post'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('posts_detail', kwargs={'post_id': self.object.id})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "post_detail.html"
    pk_url_kwarg = 'post_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('posts_detail', kwargs={'post_id': self.object.tournament_post.id})


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = "comments/add_comment.html"
    pk_url_kwarg = 'post_id'
    fields = ('comment',)

    def get_success_url(self):
        return reverse_lazy('posts_detail', kwargs={'post_id': self.object.tournament_post.id})

    def form_valid(self, form):
        data_form = form.save(commit=False)
        data_form.save()
        return JsonResponse({
            'status': 'ok',
            'comment': render_to_string('comments/add_comment.html', context={'comment': data_form})
        })

    def form_invalid(self, form):
        return JsonResponse({'status': 'fail', 'form': str(form)})


class TournamentListView(ActiveUrlMixin, ListView):
    model = Tournament
    template_name = "tournaments/tournament_list.html"
    active_url = 'tournament'


class TournamentDetailView(LoginRequiredMixin, DetailView):
    model = Tournament
    template_name = "tournaments/tournament_detail.html"
    pk_url_kwarg = 'id'


class PostEditionView(LoginRequiredMixin, UpdateView):
    model = TournamentPost
    template_name = "tournament_post_form.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('posts_detail', kwargs={'post_id': self.object.id})


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/event_list.html"


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    pk_url_kwarg = "id"
    template_name = "events/event_details.html"


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for tournament.
    """
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for tournament posts.
    """

    queryset = TournamentPost.objects.all()
    serializer_class = TournamentPostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter

    def get_queryset(self):
        return self.model.objects.all().annotate(comments_count=Count('tournament_post'), likes_count=Count('likes'))


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint for game.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

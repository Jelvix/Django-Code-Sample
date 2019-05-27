import django_filters
from django.db.models import Q

from cms.models import TournamentPost


class PostFilter(django_filters.FilterSet):
    games = django_filters.CharFilter(label='Game', field_name="game", lookup_expr='game_name__game_title__icontains')
    player = django_filters.CharFilter(label='Player', field_name="game", method='players_filter')
    winner = django_filters.CharFilter(label='Winner', field_name="game", method='winners_filter')

    order_by = django_filters.OrderingFilter(fields=['title', 'date_added', 'comments_count', 'likes_count'])

    def players_filter(self, queryset, name, value):
        return self.queryset.filter(Q(game__players__first_name__icontains=value) |
                                    Q(game__players__last_name__icontains=value) |
                                    Q(game__players__email__icontains=value))

    def winners_filter(self, queryset, name, value):
        return self.queryset.filter(Q(game__winner__first_name__icontains=value) |
                                    Q(game__winner__last_name__icontains=value) |
                                    Q(game__winner__email__icontains=value))

    search = django_filters.CharFilter(label='Search (write title or tag that you looking for)',
                                       field_name='tournament_post', method='search_filter')

    def search_filter(self, queryset, name, value):
        return self.queryset.filter(Q(title__icontains=value) |
                                    Q(tags__tag_name__icontains=value) |
                                    Q(text__icontains=value))

    class Meta:
        model = TournamentPost
        fields = ('games', 'player', 'winner')

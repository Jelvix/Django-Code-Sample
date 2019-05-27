import factory
from django.utils.datetime_safe import datetime

from accounts.tests.factory import UserModelFactory
from cms.models import Tag, Game, Tournament, TournamentPost, Comment


class GameModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    game_title = "Game"


class TournamentModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tournament

    game_name = factory.SubFactory(GameModelFactory)
    date_added = factory.LazyFunction(datetime.now)

    @factory.post_generation
    def players(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            for player in extracted:
                self.players.add(player)


class TagModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    tag_name = factory.Sequence(lambda n: 'tag{0}'.format(n))


class PostModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TournamentPost

    title = "Post"
    text = "test"
    game = factory.SubFactory(TournamentModelFactory)


class CommentModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    comment = "test"
    author = factory.SubFactory(UserModelFactory)
    tournament_post = factory.SubFactory(PostModelFactory)

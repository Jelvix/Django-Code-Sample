from django.test import TestCase
import datetime

from accounts.tests.factory import UserModelFactory
from cms.tests.factory import (TournamentModelFactory, GameModelFactory, PostModelFactory,
                               TagModelFactory, CommentModelFactory)


class TournamentModelTest(TestCase):
    def setUp(self):
        player1 = UserModelFactory()
        player2 = UserModelFactory()
        self.tournament = TournamentModelFactory(players=(player1, player2), winner=player2)

    def test_str_tournament(self):
        check = "{0}({1}:{2}:{3} winner: {4}".format(
            str(self.tournament.game_name.game_title),
            str(self.tournament.date_added.day),
            str(self.tournament.date_added.month),
            str(self.tournament.date_added.year),
            str(self.tournament.winner.email)
        )
        self.assertEqual(self.tournament.__str__(), check)


class GameModelTest(TestCase):
    def setUp(self):
        self.game = GameModelFactory()

    def test_str_game(self):
        self.assertEqual(self.game.__str__(), self.game.game_title)


class PostModelTest(TestCase):
    def setUp(self):
        self.post = PostModelFactory()
        scheduled_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
        self.post_shed = PostModelFactory(scheduled_time=scheduled_time)

    def test_str_post(self):
        check = "Title:{0}/n{1}/n like".format(str(self.post.title), self.post.text)
        self.assertEqual(self.post.__str__(), check)

    def test_is_publick(self):
        self.assertTrue(self.post.is_publish)


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = TagModelFactory()

    def test_str_tag(self):
        self.assertEqual(self.tag.__str__(), self.tag.tag_name)


class CommentModelTest(TestCase):
    def setUp(self):
        self.comment = CommentModelFactory()

    def test_str_comment(self):
        self.assertEqual(self.comment.__str__(), self.comment.comment)

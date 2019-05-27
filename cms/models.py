from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.signals import post_save
from django.utils import timezone

from cms.signal import add_first_comment

from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Game(models.Model):
    game_title = models.CharField(_('Game title'), max_length=100)

    class Meta:
        verbose_name = _('game')
        verbose_name_plural = _('games')

    def __str__(self):
        return self.game_title


class Tournament(models.Model):
    """
    This is the matches!
    Tournaments' model, custom fields:
    game_name: connection to Game model ForeignKey
    players: connection to User model ManyToMany
    winner: connection to User model ForeignKey
    date_added: date of creation model it adds automatically
    date_update: date of the last edition, it adds automatically
    """
    game_name = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_name')
    players = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='players')
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='win',
                               null=True, blank=True)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_update = models.DateTimeField(_('date update'), auto_now=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='event_match', null=True, blank=True)

    class Meta:
        verbose_name = _('tournament')
        verbose_name_plural = _('tournaments')

    def __str__(self):
        """
        Method signs the object
        :return: str of signature
        """
        result = "{0} ({1}:{2}:{3}) Winner: {4}; Players :".format(
            str(self.game_name.game_title),
            str(self.date_added.day),
            str(self.date_added.month),
            str(self.date_added.year),
            str(self.winner)
        )
        n = 0
        for player in self.players.all():
            result += ' ' + str(player)
            n += 1
            if n != self.players.all().count():
                result += ','

        return result


class TournamentPost(models.Model):
    """
    Posts' model about tournaments has custom fields:
    title: char, have to be title of the post
    text: text type, posts' body
    game: information from Tournaments model
    date_added: datetime, date of creation this post
    scheduled_time: datetime, custom field with date of publishing post
    likes: connection with Like model
    tags: connection with Tags model
    is_publish: Bool, show if this post published or not
    """
    title = models.CharField(_('title'), max_length=50)
    text = models.TextField(_('post'), max_length=1000)
    game = models.OneToOneField('Tournament', on_delete=models.CASCADE, related_name='game')
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    scheduled_time = models.DateTimeField(_('Scheduled time'), null=True, blank=True)
    likes = GenericRelation('likes.Like', related_name='post_like')
    tags = models.ManyToManyField('Tag', related_name='tag', blank=True)
    is_publish = models.BooleanField(_('is_publish'), default=False)

    class Meta:
        verbose_name = _('tournament_post')
        verbose_name_plural = _('tournament_posts')

    def __str__(self):
        """
        Show title and text
        :return: string
        """
        return "Title:{0}/n{1}/n like".format(str(self.title), self.text)

    def save(self, **kwargs):
        """
        Custom save with checking for scheduled time of publishing
        """
        if not self.scheduled_time:
            self.is_publish = True
        super(TournamentPost, self).save(**kwargs)


class Tag(models.Model):
    tag_name = models.CharField(_('tag name'), max_length=100)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.tag_name


class Comment(models.Model):
    """
    Comments' model about tournaments has custom fields:
    comment: text, body of comment
    author: ForeignKey, automatically filled with user that add comment
    tournament_post:
    """
    comment = models.TextField(_('comment'), max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_author')
    tournament_post = models.ForeignKey(TournamentPost, on_delete=models.CASCADE, related_name='tournament_post')
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    likes = GenericRelation('likes.Like', related_name=_('post like'))

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return self.comment


class Event(models.Model):
    """
    Model for event with games and matches of those games
    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='event_game')
    date_start = models.DateTimeField(_('start_date'), null=True, blank=True)
    date_finish = models.DateTimeField(_('finish_date'), null=True, blank=True)
    creation_date = models.DateTimeField(_('creation_date'), auto_now_add=True)
    date_update = models.DateTimeField(_('date_update'), auto_now=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members')

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

    @property
    def event_is_going(self):
        date_now = timezone.now()
        if self.date_start >= date_now:
            if self.date_finish < date_now:
                return True

    def __str__(self):
        return "{0} ({4}:{5} {1}/{2}/{3} - {9}:{10} {6}/{7}/{8}) ".format(str(self.game),
                                                                          self.date_start.day,
                                                                          self.date_start.month,
                                                                          self.date_start.year,
                                                                          self.date_start.hour,
                                                                          self.date_start.minute,
                                                                          self.date_finish.day,
                                                                          self.date_finish.month,
                                                                          self.date_finish.year,
                                                                          self.date_finish.hour,
                                                                          self.date_finish.minute, )


class Score(models.Model):
    """
    Score model for a one user in a particular match.
    player: ForeignKey, the player, who got a score.
    match: ForeignKey, the match in which  the player get this score
    score: PositiveIntegerField, a players' score in the match
    """
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player_score')
    match = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name='match_score')
    score = models.PositiveIntegerField(_('score'), default=0)

    class Meta:
        verbose_name = _('score')
        verbose_name = _('scores')

    def __str__(self):
        return str(self.score)


post_save.connect(add_first_comment, sender=TournamentPost)

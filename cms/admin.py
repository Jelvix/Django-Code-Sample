from django.contrib import admin

from cms.forms import TournamentForm, AdminPostForm, ScoreForm
from .models import Tournament, Game, TournamentPost, Comment, Tag, Event, Score

from tags_input import admin as tags_input_admin


class TagsAdmin(tags_input_admin.TagsInputAdmin):
    """
    Class inherited from tags_input_admin.TagsInputAdmin
    It's make it possible to write get the
    """
    list_display = ('tag_name', 'pk',)
    search_fields = ['tag_name', ]


class TournamentAdmin(admin.ModelAdmin):
    form = TournamentForm
    list_display = ('id', 'game_name', 'winner', 'date_added', 'date_update', 'event',)


class GameAdmin(admin.ModelAdmin):
    list_display = ('game_title', 'id',)


class PostAdmin(tags_input_admin.TagsInputAdmin):
    list_display = ('title', 'scheduled_time', 'text', 'game',)
    form = AdminPostForm
    readonly_fields = ('is_publish',)
    search_fields = ['tags', ]


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'author', 'tournament_post',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'date_start', 'date_finish', 'creation_date', 'date_update',)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('match', 'player', 'score',)
    form = ScoreForm


admin.site.register(Tag, TagsAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(TournamentPost, PostAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Score, ScoreAdmin)

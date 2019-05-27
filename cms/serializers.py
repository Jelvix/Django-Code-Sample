from rest_framework import serializers

from likes.serializers import LikeSerializer
from .models import Game, TournamentPost, Tournament, Comment


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('game_title',)


class TournamentPostSerializer(serializers.ModelSerializer):

    like_count = serializers.IntegerField(source='likes.count')
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = TournamentPost
        fields = ('title', 'text', 'game', 'date_added', 'scheduled_time', 'likes', 'like_count', 'tags',)


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('game_name', 'players', 'winner', 'date_added', 'date_update',)


class CommentSerializer(serializers.ModelSerializer):

    like_count = serializers.IntegerField(source='likes.count')
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('comment', 'author', 'tournament_post', 'date_added', 'likes', 'like_count', )

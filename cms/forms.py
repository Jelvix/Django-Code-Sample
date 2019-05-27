from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from tags_input.fields import TagsInputField
from ckeditor.widgets import CKEditorWidget
from tags_input.widgets import TagsInputWidget

from cms.models import Comment, Tournament, TournamentPost, Tag, Score


class CommentForm(forms.ModelForm):
    tournament_post = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    author = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'style': 'height:50px; width:100%',
                                                                     'placeholder': _('Comment')}))

    class Meta:
        model = Comment
        fields = ('comment', 'author', 'tournament_post')


class TournamentForm(forms.ModelForm):

    def clean_players(self):
        players = self.cleaned_data['players']
        if len(players) != 2:
            raise ValidationError('Too many characters ...')
        return players

    def clean(self):
        cleaned_data = super(TournamentForm, self).clean()
        winner = cleaned_data['winner']
        if winner not in cleaned_data.get('players', list()):
            return self.add_error('winner', _('Winner is not in players'))
        return cleaned_data

    class Meta:
        model = Tournament
        fields = ('game_name', 'players', 'winner', 'event')


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('match', 'player', 'score')

    def clean(self):
        cleaned_data = super(ScoreForm, self).clean()
        match = cleaned_data['match']
        player = cleaned_data['player']
        if player not in match.players.all():
            return self.add_error('player', _('Player is not in match'))
        return cleaned_data


class PostForm(forms.ModelForm):
    """
    Form for posts that embed texts' redactor
    """
    text = forms.CharField(widget=CKEditorWidget())
    tags = TagsInputField(widget=TagsInputWidget(), queryset=Tag.objects.all(), create_missing=True, required=True, )

    class Meta:
        model = TournamentPost
        fields = ('title', 'text', 'game', 'scheduled_time', 'tags',)


class AdminPostForm(forms.ModelForm):
    """
    Form for posts in admin version that embed texts' redactor
    """
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = TournamentPost
        fields = '__all__'

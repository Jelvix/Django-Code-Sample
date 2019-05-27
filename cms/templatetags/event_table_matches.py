from django import template
from django.utils.safestring import mark_safe

from cms.models import Tournament, Score

register = template.Library()


@register.simple_tag
def win_fail_none(player, played_with, event_id):
    if player != played_with:
        match = Tournament.objects.filter(event=event_id, players__in=[player]).filter(players__in=[played_with])
        if match.exists():
            match = match.first()
            if match.winner is not None:
                scores = Score.objects.filter(match=match.id)
                if scores.first() is not None:
                    player_s = scores.filter(player=player).first()
                    if player_s is None:
                        player_score = 0
                    elif player_s:
                        player_score = player_s.score
                    opponent_s = scores.filter(player=played_with).first()
                    if opponent_s is None:
                        opponent_score = 0
                    elif opponent_s:
                        opponent_score = opponent_s.score
                    return str(player_score) + ':' + str(opponent_score)
                elif match.winner.id == player:
                    return "W"
                elif match.winner.id == played_with:
                    return "L"
            else:
                return "R"

        else:
            return mark_safe('<span class="glyphicon glyphicon-hourglass"></span>')
    else:
        return mark_safe('<span class="glyphicon glyphicon-remove"></span>')


@register.simple_tag
def match_id(player1, player2, event):
    match = Tournament.objects.filter(event=event, players__in=[player2]).filter(players__in=[player1])
    if match.exists() and player2 != player1:
        return match.first().id
    else:
        return

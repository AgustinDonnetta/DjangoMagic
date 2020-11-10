from django import forms

from .models import Player, Match, Turn

class PlayerUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['full_name','DNI','born_date','image','is_active']

class MatchCreateForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['player_1','player_2','date','winner','status_2']

class TurnCreateForm(forms.ModelForm):
    class Meta:
        model = Turn
        fields = ['match','turn_number','player','play_land','play_creatures','play_another_thing','attack','player_1_life','player_2_life']

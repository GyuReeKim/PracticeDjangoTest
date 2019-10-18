from django import forms
from .models import Music, Favor

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'

class FavorForm(forms.ModelForm):
    favors = [(1, '1번'), (2, '2번')]
    pick = forms.ChoiceField(choices=favors, widget=forms.RadioSelect)
    class Meta:
        model = Favor
        fields = ('pick', 'comment',)
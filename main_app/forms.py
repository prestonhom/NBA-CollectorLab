from django.forms import ModelForm, Select
from .models import Team, Player

class PlayerForm(ModelForm):
    class Meta:
        model= Player
        fields = '__all__'
       
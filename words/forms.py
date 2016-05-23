from django.forms import ModelForm
from words.models import Row


class GameForm(ModelForm):

    class Meta:
        model = Row
        exclude = ['letter']

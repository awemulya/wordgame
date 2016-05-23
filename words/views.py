import random
import string

from django.shortcuts import render

from words.models import Row
from words.forms import GameForm


def index(request):
    rows = Row.objects.order_by('letter')[:26]
    context = {'rows': rows}
    return render(request, 'words/index.html', context)


def create_new(letters, count=1):
    letter = random.choice(string.ascii_lowercase)
    if count > 26:
        return 'a'
    if not letter in letters:
        return letter
    else:
        return create_new(letters, count+1)


def play(request):
    rows = Row.objects.all()
    letters = [l.letter for l in rows]
    letter = create_new(letters)
    context = {'letter': letter, 'form':GameForm()}
    return render(request, 'words/play.html', context)
import random
import string

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
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
    context = {'letter': letter, 'form':GameForm(initial={'letter':letter})}
    return render(request, 'words/play.html', context)


def save(request):
    form = GameForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('words:index'))

from django import forms
from django.forms import ModelForm
from words.models import Row


class GameForm(ModelForm):

    class Meta:
        model = Row
        exclude = []
        widgets = {'letter': forms.HiddenInput()}

    def save(self, commit=True):
        instance = super(GameForm,self).save(commit=False)
        l = getattr(instance,'letter')
        fields = [f.name for f in Row._meta.get_fields()]
        for field in fields:
            if field not in ['id','letter'] and not getattr(instance,field).startswith(l):
                setattr(instance,field,'')
        if commit:
            instance.save()
        return instance

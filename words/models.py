from __future__ import unicode_literals

from django.db import models


class Row(models.Model):
    letter = models.CharField(max_length=256)
    name = models.CharField(max_length=256,blank=True,null=True)
    cast = models.CharField(max_length=256,blank=True,null=True)
    country = models.CharField(max_length=256,blank=True,null=True)
    food = models.CharField(max_length=256,blank=True,null=True)
    animal = models.CharField(max_length=256,blank=True,null=True)

    def __str__(self):
        return self.letter

    def score(self):
        count = 0
        fields = [f.name for f in Row._meta.get_fields()]
        for field in fields:
            if getattr(self,field) and field not in ['letter', 'id']:
                count +=1
        return count

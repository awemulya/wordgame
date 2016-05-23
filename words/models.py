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

from django.db import models


class John(models.Model):
    name = models.CharField(max_length=100, blank=True, default="")
    consumed_food = models.ManyToManyField('Bacon', blank=True, related_name='eater')


class Bacon(models.Model):
    description = models.CharField(max_length=42)

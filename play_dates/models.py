__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.db import models


class PlayDate(models.Model):
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    children = models.ManyToManyField(
        'children.Child',
        through='play_dates.PlayDateChild',
        through_fields=('play_date', 'children'),
        related_name='play_dates'
    )


class PlayDateChild(models.Model):
    play_date = models.ForeignKey('play_dates.PlayDate')
    children = models.ForeignKey('children.Child')

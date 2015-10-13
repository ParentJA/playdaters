# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_dt', models.DateTimeField()),
                ('end_dt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayDateChild',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('children', models.ForeignKey(to='children.Child')),
                ('play_date', models.ForeignKey(to='play_dates.PlayDate')),
            ],
        ),
        migrations.AddField(
            model_name='playdate',
            name='children',
            field=models.ManyToManyField(related_name='play_dates', through='play_dates.PlayDateChild', to='children.Child'),
        ),
    ]

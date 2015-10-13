# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default=b'U', max_length=1, choices=[(b'M', b'male'), (b'F', b'female'), (b'U', b'unspecified')])),
                ('photo', models.ImageField(default=b'photos/no-image.jpg', null=True, upload_to=b'photos', blank=True)),
                ('parent', models.ForeignKey(related_name='children', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

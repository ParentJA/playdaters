__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to='photos', default='photos/no-image.jpg', blank=True, null=True)

    @property
    def photo_url(self):
        try:
            return self.photo.url
        except ValueError:
            return None

    def __unicode__(self):
        return self.get_full_name()

__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL')

GENDER = (
    ('M', 'male'),
    ('F', 'female'),
    ('U', 'unspecified'),
)


class Child(models.Model):
    parent = models.ForeignKey(AUTH_USER_MODEL, related_name='children')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='U')
    photo = models.ImageField(upload_to='photos', default='photos/no-image.jpg', blank=True, null=True)

    @property
    def photo_url(self):
        try:
            return self.photo.url
        except ValueError:
            return None

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

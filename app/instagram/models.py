from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.user

class Gallery(models.Model):
    tag = models.CharField(max_length=100)
    owner = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.tag

class Photo(models.Model):
    ig_url = models.URLField()
    photo_url = models.URLField()

    gallery = models.ForeignKey(Gallery)

    blocked = models.BooleanField(default=False)

    def __unicode__(self):
        return self.ig_url, self.photo_url


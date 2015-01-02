import requests

from django.conf import settings
from django.contrib.auth.models import User

from app.celery import app
from .models import Gallery, Photo, Customer

@app.task
def task():
    print 'Hello, world!'
    return 'Returned hello!'

@app.task
def create_gallery(tag, customer):
    gallery = Gallery(tag=tag, owner=customer)
    gallery.save()

    ig_id = settings.INSTAGRAM_ID
    tag_url = "https://api.instagram.com/v1/tags/"\
              +tag+"/media/recent?client_id="\
              +ig_id

    req = requests.get(tag_url)
    #print req.text
    data = req.json()['data']
    photos = []
    for item in data:
        photos.append(Photo(ig_url=item['link'],
              photo_url=item['images']['low_resolution']['url'],
              gallery=gallery))
    Photo.objects.bulk_create(photos)

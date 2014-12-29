from app.celery import app
from django.contrib.auth.models import User

from .models import Gallery, Photo, Customer

@app.task
def task():
    print 'Hello, world!'
    return 'Returned hello!'

@app.task
def create_gallery():
    print 'Helo'
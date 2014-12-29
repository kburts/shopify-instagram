from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Customer, Gallery, Photo

class PhotoSerializer(serializers.ModelSerializer):
    #ig_url = serializers.Serializer()
    class Meta:
        model = Photo
        fields = ('ig_url', 'photo_url', 'blocked')



class GallerySerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    class Meta:
        model = Gallery
        fields = ('tag', 'owner', 'photos',)
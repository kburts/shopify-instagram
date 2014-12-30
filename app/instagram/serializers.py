from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Customer, Gallery, Photo

class PhotoSerializer(serializers.ModelSerializer):
    #ig_url = serializers.Serializer()
    class Meta:
        queryset = Photo.objects.all().filter(blocked=True)
        model = Photo
        fields = ('ig_url', 'photo_url', 'blocked')



class GallerySerializer(serializers.ModelSerializer):
    queryset = Photo.objects.all().filter(blocked=True)
    photos = PhotoSerializer(queryset, many=True)
    owner = serializers.StringRelatedField()
    #photos = serializers.Serializer(Photo.objects.all())
    class Meta:
        model = Gallery
        fields = ('tag', 'owner', 'photos',)
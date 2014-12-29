from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Customer, Gallery, Photo

class PhotoSerializer(serializers.ModelSerializer):
    #ig_url = serializers.Serializer()
    class Meta:
        model = Photo
        #fields = ('ig_url',)



class GallerySerializer(serializers.ModelSerializer):
    #photos = serializers.StringRelatedField(many=True)
    #photos = serializers.ReadOnlyField(source='photo_set')
    #photo_set = serializers.Serializer(many=True, source='ob')
    #photo_set = PhotoSerializer()
    photos = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Gallery
        fields = ('tag', 'owner', 'photos',)
        #depth = 1
        #fields = ('tag', 'owner')
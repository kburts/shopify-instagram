from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from .models import Customer, Gallery, Photo
from .serializers import GallerySerializer
# Create your views here.

class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    permission_classes = (permissions.AllowAny,)

class GalleryDetail(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    lookup_field = 'tag'

from django.contrib.auth.models import User

# CBV
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status

# GCBV
from rest_framework import generics
from rest_framework import permissions

from .models import Customer, Gallery, Photo
from .serializers import GallerySerializer, GalleryCreateSerializer
from .permissions import IsOwnerOrReadOnly
from .tasks import create_gallery
# Create your views here.

class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    permission_classes = (permissions.AllowAny,)

class GalleryDetail(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    lookup_field = 'tag'

class CreateGallery(APIView):
    #permission_classes = (IsOwnerOrReadOnly,)

    #serializer_class = GallerySerializer

    def post(self, request, format=None):
        serializer = GalleryCreateSerializer(data=request.data)
        if serializer.is_valid():
            #print serializer.data
            #print repr(serializer)
            create_gallery(tag=serializer.data['tag'], customer=Customer.objects.all()[0])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    def get(self, request, format=None):
        galleries = Gallery.objects.values()
        serializer = GallerySerializer(data=galleries)
        if serializer.is_valid():
            print repr(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
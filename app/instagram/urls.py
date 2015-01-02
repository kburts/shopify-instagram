from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import GalleryList, GalleryDetail, CreateGallery

urlpatterns = patterns('',
    url(r'gallery/$', GalleryList.as_view(), name='gallery-list'),
    url(r'gallery/(?P<tag>[0-9a-zA-Z_-]+)/$', GalleryDetail.as_view(), name='gallery-detail'),
    url(r'gallerycreate/$', CreateGallery.as_view(), name='gallery-create'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import GalleryList

urlpatterns = patterns('',
    url(r'gallery/$', GalleryList.as_view(), name='gallery-list'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
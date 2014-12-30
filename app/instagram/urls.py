from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import GalleryList, GalleryDetail

urlpatterns = patterns('',
    url(r'gallery/$', GalleryList.as_view(), name='gallery-list'),
    url(r'gallery/(?P<tag>[0-9a-zA-Z_-]+)/$', GalleryDetail.as_view(), name='gallery-detail')
)

urlpatterns = format_suffix_patterns(urlpatterns)
"""amenityFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import re

import rest_framework_swagger.urls
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework.routers import DefaultRouter

from location.views import LocationViewSet
from post.views import PostViewSet, PictureViewSet
from account.views import AccountViewSet, UserViewSet
from .views import index

router = DefaultRouter()
router.register('location', LocationViewSet, base_name='location')
router.register('post', PostViewSet, base_name='post')
router.register('picture', PictureViewSet, base_name='picture')
router.register('account', AccountViewSet, base_name='account')
router.register('user', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-docs/', include(rest_framework_swagger.urls, namespace='api-docs')),
]

# Fail safe! If nginx is down, this might come handy.
urlpatterns += [
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve,
        kwargs={
            'document_root': settings.STATIC_ROOT,
        }
        ),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve,
        kwargs={
            'document_root': settings.MEDIA_ROOT,
        }
        ),
]

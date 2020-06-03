from django.conf.urls import url
from django.urls import path, include
from . import views
urlpatterns = [
    url(r'^$', views.index, name='registration'),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    path('', include('info.urls') ,name='information')
]

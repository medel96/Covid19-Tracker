from django.urls import path,include
from . import views

urlpatterns = [
    path('uti_list/',views.uti_list, name='uti_list'),
    path('uti_new/', views.uti_new, name='uti_new'),
    path('cherche/',views.chercher),
]


from django.urls import path,include
from . import views

urlpatterns = [
    path('moroccan_plots/', views.moroccan_plots , name="moroccan_plots"),
    path('world_plots/', views.world_plots , name="world_plots"),

]

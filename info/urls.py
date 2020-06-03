
from django.urls import path,include
from . import views

alpha = ""
urlpatterns = [
    path('information/', views.information, name="information"),
    path('world/', views.world , name="world"),
    path('country/', views.country , name="country"),
    path('', include('plots.urls') ,name='plots'),
    path('', include('symptom_form.urls') ,name='symptom_form')

    # path('nations<str:alpha>', views.nations)
]

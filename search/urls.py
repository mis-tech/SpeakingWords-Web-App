from django.urls import path
from . import views

urlpatterns = [

    path('Search', views.Search, name="search"),
    
]

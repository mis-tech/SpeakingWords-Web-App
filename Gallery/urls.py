from django.urls import path
from . import views

urlpatterns = [
    path('Gallery',views.Gallery, name="gallery"),
]

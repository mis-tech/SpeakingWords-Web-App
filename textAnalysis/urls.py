from django.urls import path
from . import views

urlpatterns = [

    path('Text_Processing', views.Text_Processing, name="Text_Processing"),
    
]

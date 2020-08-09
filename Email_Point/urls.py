from django.urls import path
from . import views

urlpatterns = [

    path('Send_Email', views.Send_Email, name="Send_Email"),

]

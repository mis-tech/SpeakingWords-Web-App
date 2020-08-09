from django.urls import path
from . import views

urlpatterns = [

    path('', views.home,name='home'),
    path('help', views.help,name='help'),
    path('Dashboard', views.Dashboard, name="dashboard"),
]

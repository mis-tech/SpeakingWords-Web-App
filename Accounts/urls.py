from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from Accounts import views


urlpatterns = [

    path('register/', views.register, name="register_url"),
    path('login/', LoginView.as_view(),name="login_url"),
    path('About/', views.About,name="About"),
    path('Accounts/', include('django.contrib.auth.urls')),
]
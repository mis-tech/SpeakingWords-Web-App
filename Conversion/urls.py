from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"),
    path('ManualText',views.ManualTxt, name="ManualTxt"),
    path('External_Text',views.External_Text, name="External_Text"),
    path('File_Upload',views.File_Upload, name="File_Upload"),
]
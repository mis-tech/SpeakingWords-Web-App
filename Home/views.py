from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request,'index.html')


def help(request):
	return render(request,'help.html')


def Dashboard(request):
	return render(request, 'dashboard.html')








from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



@login_required
def dashboardView(request):
	return render(request, 'index.html')

def register(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')
	else:
		form=UserCreationForm()
	return render(request,'registration/register.html',{'form':form})
	

def About(LoginRequiredMixin, request):
	return render(request,'About.html',name="About")
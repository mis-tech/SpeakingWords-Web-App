from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def Send_Email(request):
	if request.method == "POST":
		if request.POST['submit'] == 'AuthSending':
			message_name = request.POST['message_name']
			message = request.POST['message']

			send_mail(
				'Contact Form',
				message,
				settings.EMAIL_HOST_USER,
				['erumshehzadihere@gmail.com'],
				fail_silently=False
				)
			return render(request, 'index.html',{'message_name':message_name})

		if request.POST['submit'] == 'NewSending':
			message_name = request.POST['message_name']
			message_email = request.POST['message_email']
			message = request.POST['message']
			send_mail(
				message_name,
				message,
				message_email,
				['erumshehzadihere@gmail.com'],
				)
			return render(request, 'index.html',{'message_name':message_name})
	else:
		return render(request, 'index.html',{})
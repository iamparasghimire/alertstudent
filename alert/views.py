from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.


def home(request):
 
    return render(request, 'alert/index.html')





def contact(request):

    if request.method == 'POST':

        template = render_to_string('system/contact.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['shisir1924@gmail.com']
        )

        email.fail_silently = False
        email.send()

    return render(request, 'alert/contact.html')


def register(request):
    return render(request, 'alert/register.html')


def password(request):
    return render(request, 'alert/password.html')


def login(request):
    return render(request, 'alert/login.html')
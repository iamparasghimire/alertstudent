from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
# Create your views here.


def home(request):
 
    return render(request, 'alert/index.html')





def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, email,subject, message)

        if len(name)<2 or len(email)<3  or len(message)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,subject=subject, message=message)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

   

    return render(request, 'alert/contact.html')


def register(request):
    return render(request, 'alert/register.html')


def password(request):
    return render(request, 'alert/password.html')


def login(request):
    return render(request, 'alert/login.html')
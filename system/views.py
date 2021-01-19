from django.shortcuts import render, redirect
from system.forms import noticeForm

from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import noticeForm, tableForm, notesForm
from .models import *

# Create your views here.


def home(request):
 
    return render(request, 'system/index.html')


def chart(request):
    return render(request, 'system/charts.html')


def table(request):
    return render(request, 'system/tables.html')


def note(request):
    return render(request, 'system/note.html')


def notesingle(request):
    all_notes = models.notes.objects.all()
    context = {'data', all_notes}
    return render(request, 'system/notesingle.html')


def notice(request):
    return render(request, 'system/notice.html')


def createtable(request):
    form = tableForm()
    if request.method == 'POST':
        form = tableForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'system/createdetails.html', context)


def createnotes(request):
    form = notesForm()
    if request.method == 'POST':
        form = notesForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'system/createnotes.html', context)


def createnotice(request):
    form = noticeForm()
    if request.method == 'POST':
        form = noticeForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'system/createnotice.html', context)


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

    return render(request, 'system/contact.html')


def register(request):
    return render(request, 'system/register.html')


def password(request):
    return render(request, 'system/password.html')


def login(request):
    return render(request, 'system/login.html')

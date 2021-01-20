from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import noticeForm, tableForm, noteForm

# Create your views here.


def home(request):
 
    return render(request, 'alert/index.html')


def chart(request):
    return render(request, 'alert/charts.html')


def table(request):
    all_table = models.table.objects.all()
    context = {'tables': all_table}

    return render(request, 'alert/tables.html',context)


def note(request):
    return render(request, 'alert/note.html')


def notesingle(request):
    all_note = models.note.objects.all()
    context = {'data': all_note}
    return render(request, 'alert/notesingle.html',context)


def notice(request):
    all_notice = models.notice.objects.all()
    context = {'notices': all_notice}
    return render(request, 'alert/notice.html',context)


def createtable(request):
    form = tableForm()
    if request.method == 'POST':
        form = tableForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'alert/createdetails.html', context)


def createnote(request):
    form = noteForm()
    if request.method == 'POST':
        form = noteForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'alert/createnotes.html', context)


def createnotice(request):
    form = noticeForm()
    if request.method == 'POST':
        form = noticeForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'alert/createnotice.html', context)


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
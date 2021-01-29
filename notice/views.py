from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notice
from django.contrib import messages
from .forms import NoticeForm
from . import models


def notice(request):
    all_notice = models.Notice.objects.all()
    context = {'notices': all_notice}
    return render(request, 'notice/notice.html',context)


def createnotice(request):
    form = NoticeForm()
    if request.method =='POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/notice/')
            return HttpResponse('Thank you')
            messages.add_message(request, messages.INFO, 'Hello world.')

    context = {'form':form}
    return render(request, 'notice/createnotice.html',context)


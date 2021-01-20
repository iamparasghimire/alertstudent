from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse

from .forms import noticeForm

# Create your views here.







def notice(request):
    all_notice = models.notice.objects.all()
    context = {'notices': all_notice}
    return render(request, 'notice/notice.html',context)







def createnotice(request):
    form = noticeForm()
    if request.method == 'POST':
        form = noticeForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'notice/createnotice.html', context)


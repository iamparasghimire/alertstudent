from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse


# Create your views here.







def notice(request):
    all_notice = models.notice.objects.all()
    context = {'notices': all_notice}
    return render(request, 'notice/notice.html',context)







def createnotice(request):
  
    return render(request, 'notice/createnotice.html')


from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .models import Notice
from django.contrib import messages

# Create your views here.







def notice(request):
    all_notice = models.Notice.objects.all()
    context = {'notices': all_notice}
    return render(request, 'notice/notice.html',context)







def createnotice(request):
    if request.method=='POST':
        description = request.POST['description']
        image = request.POST['image']
        date = request.POST['date']
        print(description, image,date)

        if len(description)<2 :
            messages.error(request, "Please fill the form correctly")
        else:
            notice = Notice(description=description, image=image,date=date)
            notice.save()
            messages.success(request, "Your message has been successfully sent")
  
    return render(request, 'notice/createnotice.html')


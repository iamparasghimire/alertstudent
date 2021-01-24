from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .models import Table
from django.contrib import messages
# Create your views here.




def table(request):
    all_table = models.Table.objects.all()
    context = {'tables': all_table}

    return render(request, 'studenttable/tables.html',context)





def createtable(request):
    if request.method=='POST':
        name = request.POST['name']
        faculty = request.POST['faculty']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        batch = request.POST['batch']
        email = request.POST['email']
        print(name,faculty, address1,address2,batch)

        if len(name)<2 or len(faculty)<2 or len(address1)<2 :
            messages.error(request, "Please fill the form correctly")
        else:
            table = Table(name=name, faculty=faculty,address1=address1,address2=address2,batch=batch,email=email)
            table.save()
            messages.success(request, "Your message has been successfully sent")
  

    return render(request, 'studenttable/createdetails.html')


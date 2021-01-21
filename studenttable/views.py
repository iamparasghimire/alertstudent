from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse

# Create your views here.




def table(request):
    all_table = models.table.objects.all()
    context = {'tables': all_table}

    return render(request, 'studenttable/tables.html',context)





def createtable(request):

    return render(request, 'studenttable/createdetails.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib import messages
# Create your views here.
from .forms import TableForm


def table(request):
    all_table = models.Table.objects.all()
    context = {'tables': all_table}
    return render(request, 'studenttable/tables.html', context)

def createtable(request):
    form = TableForm()
    if request.method =='POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Details has been saved.')
            return redirect('/studenttable/')
    context = {'form':form}
    return render(request, 'studenttable/createdetails.html',context)
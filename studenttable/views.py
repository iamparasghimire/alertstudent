from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib import messages
# Create your views here.
from .forms import TableForm
from django.shortcuts import render, get_object_or_404
from .forms import TableForm
from .models import Table

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

def edittable(request, id):
    instance = get_object_or_404(Table, id=id)
    form = TableForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student Details has been updated.')
        return redirect('/studenttable/')
    return render(request, 'studenttable/createdetails.html', {'form': form})

def deletetable(request,id):
    student = get_object_or_404(Table, id=id)
    if request.method == 'GET':
        student.delete()
        messages.success(request, 'Student Details has been deleted.')
    return redirect('/studenttable/')
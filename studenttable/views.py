from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .forms import tableForm

# Create your views here.




def table(request):
    all_table = models.table.objects.all()
    context = {'tables': all_table}

    return render(request, 'studenttable/tables.html',context)





def createtable(request):
    form = tableForm()
    if request.method == 'POST':
        form = tableForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'studenttable/createdetails.html', context)


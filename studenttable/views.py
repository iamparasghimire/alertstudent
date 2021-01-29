from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
<<<<<<< HEAD
=======
from notes.models import Faculty
>>>>>>> 474657f845c5d4d813fd4a44ea1c84e487025b07
from django.contrib import messages
from .forms import student_form
# Create your views here.
<<<<<<< HEAD
from .forms import TableForm
=======
>>>>>>> 474657f845c5d4d813fd4a44ea1c84e487025b07


def table(request):
    all_table = models.Table.objects.all()
    context = {'tables': all_table}
    return render(request, 'studenttable/tables.html', context)

def createtable(request):
<<<<<<< HEAD
    form = TableForm()
    if request.method =='POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/studenttable/')
    context = {'form':form}

=======
    if request.method == 'POST':
        form = student_form(request.POST)
        name            = request.POST['name']
        faculty1        = request.POST['faculty']
        semester        = request.POST['semester']
        address1        = request.POST['address1']
        address2        = request.POST['address2']
        batch           = request.POST['batch']
        email           = request.POST['email']
        semester_list   = ['1','2','3','4','5','6','7','8']
        print("seemster is ",semester)
        if semester in semester_list:
            if len(name) < 2 or len(address1) < 2:
                messages.error(request, "Please fill the form correctly")
            else:
                table = models.Table(name=name, semester=semester, address1=address1,
                            address2=address2, batch=batch, email=email,faculty=faculty1)
                table.save()
                messages.success(
                    request, "Your message has been successfully sent")
        else:
            messages.error(request, "Error: Invalid Semester Id Supplied.")
    all_fac = Faculty.objects.all()
    form = student_form()
    context = {'faculty': all_fac,'form':form}
>>>>>>> 474657f845c5d4d813fd4a44ea1c84e487025b07
    return render(request, 'studenttable/createdetails.html',context)
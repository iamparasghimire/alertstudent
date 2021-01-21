from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse


# Create your views here.





def note(request):
    return render(request, 'notes/note.html')

def faculty(request):
    return render(request, 'notes/faculty.html')


def notesingle(request):
    all_note = models.note.objects.all()
    context = {'data': all_note}
    return render(request, 'notes/notesingle.html',context)





def createnote(request):
 
    context = {}
    return render(request, 'notes/createnotes.html', context)


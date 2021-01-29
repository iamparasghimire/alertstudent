from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .models import Note
from django.contrib import messages
# Create your views here.
from .forms import NoteForm




def note(request):
    all_notes = models.Note.objects.all()
    context = {'data': all_notes}
    return render(request, 'notes/note.html',context)

def faculty(request):
    all_faculties = models.Faculty.objects.all()
    context = {'faculties': all_faculties}
    return render(request, 'notes/faculty.html',context)


def notesingle(request):
    all_notes = models.Note.objects.all()
    context = {'data': all_notes}

    return render(request, 'notes/notesingle.html',context)





def createnote(request):
    form = NoteForm()
    if request.method =='POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/note/notesingle/')
    context = {'form':form}
    return render(request, 'notes/createnotes.html',context)


from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse

from notes.forms import noteForm

# Create your views here.





def note(request):
    return render(request, 'notes/note.html')


def notesingle(request):
    all_note = models.note.objects.all()
    context = {'data': all_note}
    return render(request, 'notes/notesingle.html',context)





def createnote(request):
    form = noteForm()
    if request.method == 'POST':
        form = noteForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'notes/createnotes.html', context)


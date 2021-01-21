from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .models import Note
from django.contrib import messages

# Create your views here.





def note(request):
    return render(request, 'notes/note.html')

def faculty(request):
    return render(request, 'notes/faculty.html')


def notesingle(request):
    all_note = models.Note.objects.all()
    context = {'data': all_note}
    return render(request, 'notes/notesingle.html',context)





def createnote(request):
    if request.method=='POST':
        semester = request.POST['semester']
        title = request.POST['title']
        docfile = request.POST['file']
        description = request.POST['description']
        print(semester, title,docfile,description)

        if len(title)<3 or len(description)<5 :
            messages.error(request, "Please fill the form correctly")
        else:
            note = Note(semester=semester, title=title,description=description,docfile=docfile)
            note.save()
            messages.success(request, "Your message has been successfully sent")
 
   
    return render(request, 'notes/createnotes.html')


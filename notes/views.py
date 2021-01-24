from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .models import Note
from django.contrib import messages
# Create your views here.





def note(request):
    all_notes = models.Note.objects.all()
    context = {'data': all_notes}
    return render(request, 'notes/note.html',context)

def faculty(request):
    all_faculties = models.Faculty.objects.all()
    notes = all_faculties.notes_set.all()
    context = {'faculties': all_faculties}
    return render(request, 'notes/faculty.html',context)


def notesingle(request):
    all_notes = models.Note.objects.all()
    context = {'data': all_notes}

    return render(request, 'notes/notesingle.html',context)





def createnote(request):
    if request.method=='POST':
        semester = request.POST['semester']
        faculty= request.POST['faculty']
        subject = request.POST['subject']
        docfile = request.POST['file']
        description = request.POST['description']
        print(semester, faculty,subject,docfile,description)

        if len(subject)<1 or len(description)<5 :
            messages.error(request, "Please fill the form correctly")
        else:
            note = Note(semester=semester,faculty=faculty, subject=subject,docfile=docfile,description=description)
            note.save()
            messages.success(request, "Your message has been successfully sent")
 
   
    return render(request, 'notes/createnotes.html')


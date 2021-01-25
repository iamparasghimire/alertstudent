from notes.models import Faculty
from django import forms

class student_form(forms.Form):
    name        = forms.CharField(label='name', max_length=100)
    email       = forms.EmailField(label='email')
    address1    = forms.CharField(label='address1',max_length=100)
    address2    = forms.CharField(label='address2',max_length=100)
    Faculty     = forms.CharField(max_length=3)
    '''
    faculty
    semester
    batch
    '''
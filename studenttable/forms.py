from django import forms
from .models import Table

class TableForm(forms.ModelForm):
    class Meta(object):
        model = Table
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(TableForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['faculty'].widget.attrs.update({'class' : 'form-control'})
        self.fields['semester'].widget.attrs.update({'class' : 'form-control'})
        self.fields['permanent'].widget.attrs.update({'class' : 'form-control'})
        self.fields['phone'].widget.attrs.update({'class' : 'form-control'})
        self.fields['batch'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
from django.forms import ModelForm
from notes.models import note



class noteForm(ModelForm):
    class Meta:
        model = note
        fields = '__all__'

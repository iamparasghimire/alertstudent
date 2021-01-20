from django.forms import ModelForm
from .models import table

class tableForm(ModelForm):
    class Meta:
        model = table
        fields = '__all__'
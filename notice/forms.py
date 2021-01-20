from django.forms import ModelForm
from .models import notice

class noticeForm(ModelForm):
    class Meta:
        model = notice
        fields = '__all__'
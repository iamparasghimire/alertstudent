from django.forms import ModelForm
from .models import notice
from .models import table
from .models import note


class noticeForm(ModelForm):
    class Meta:
        model = notice
        fields = '__all__'
class tableForm(ModelForm):
    class Meta:
        model = table
        fields = '__all__'
class noteForm(ModelForm):
    class Meta:
        model = note
        fields = '__all__'

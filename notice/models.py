from django.db import models
from django.forms import ModelForm

# Create your models here.
class Notice(models.Model):
    description = models.TextField(max_length=254)
    image = models.FileField(upload_to=None, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url=''
        return url
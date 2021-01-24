from django.db import models

# Create your models here.
class Notice(models.Model):
    description = models.TextField()
    image = models.FileField(upload_to=None, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url=''
        return url
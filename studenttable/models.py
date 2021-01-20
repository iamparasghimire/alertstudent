from django.db import models

# Create your models here.
class table(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)
    faculty = models.CharField(max_length=155, null=True, blank=True)
    address1 = models.CharField(max_length=80, null=True, blank=True)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    batch = models.CharField(max_length=85, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

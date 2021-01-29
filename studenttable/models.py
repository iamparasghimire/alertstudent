from django.db import models
from notes.models import Faculty
# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    STATUS = {
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
        ('6', 'Sixth'),
        ('7', 'Seventh'),
        ('8', 'Eighth'),
    }
    semester = models.CharField(max_length=200, choices=STATUS)
<<<<<<< HEAD
    permanent = models.CharField(max_length=80, null=True, blank=True)
    phone = models.CharField(max_length=80, null=True, blank=True)
=======
    address1 = models.CharField(max_length=80, null=True, blank=True)
    address2 = models.CharField(max_length=80, null=True, blank=True)
>>>>>>> 474657f845c5d4d813fd4a44ea1c84e487025b07
    batch = models.CharField(max_length=85, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

from django.db import models

# Create your models here.
class grade(models.Model):
    grade = models.CharField(max_length=155)
    description = models.CharField(max_length=200, null=True, blank=True)


class note(models.Model):
    sem = models.IntegerField()
    title = models.CharField(max_length=155)
    docfile = models.FileField()
    description = models.CharField(max_length=2000,null=True, blank=True)
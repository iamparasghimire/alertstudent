from django.db import models

# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Note(models.Model):
    STATUS = {
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
        ('Fourth', 'Fourth'),
        ('Fifth', 'Fifth'),
        ('Sixth', 'Sixth'),
        ('Seventh', 'Seventh'),
        ('Eighth', 'Eighth'),
    } #Yesko ta value eutai huncha haina aaba. Yeslai 1,2,3,4 banau/
    semester = models.CharField(max_length=200, choices=STATUS)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.CharField(max_length=155)
    docfile = models.FileField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject
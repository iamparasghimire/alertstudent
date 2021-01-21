from django.db import models


class table(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)
    faculty = models.CharField(max_length=155, null=True, blank=True)
    address1 = models.CharField(max_length=80, null=True, blank=True)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    batch = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)


class grade(models.Model):
    grade = models.CharField(max_length=155)
    description = models.CharField(max_length=200, null=True, blank=True)


class note(models.Model):
    sem = models.IntegerField()
    title = models.CharField(max_length=155)
    docfile = models.FileField()
    description = models.TextField(null=True, blank=True)


class notice(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to=None, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

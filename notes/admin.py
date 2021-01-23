from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Note)
admin.site.register(Faculty)
admin.site.register(Semester)


from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(note)
admin.site.register(grade)


from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(table)
admin.site.register(grade)
admin.site.register(note)
admin.site.register(notice)
admin.site.register(contact)
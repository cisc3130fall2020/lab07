from django.contrib import admin
from .models import *

# Register your models here.
class LabAdmin(admin.ModelAdmin):
    model = Lab

admin.site.register(Lab, LabAdmin)    

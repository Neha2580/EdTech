from django.contrib import admin
from .models import doctorinfo

class docfn(admin.ModelAdmin):
    list_display = ("docName", "expertise", "contact",)

admin.site.register(doctorinfo, docfn)

# Register your models here.

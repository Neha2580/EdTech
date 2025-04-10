from django.contrib import admin
from .models import positions

class posfn(admin.ModelAdmin):
    list_display = ("positionname", "baseSalary", "department",)

admin.site.register(positions, posfn)
# Register your models here.

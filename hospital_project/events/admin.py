from django.contrib import admin
from .models import events

class evefn(admin.ModelAdmin):
    list_display = ("eventname", "organizer",)

admin.site.register(events, evefn)

# Register your models here.

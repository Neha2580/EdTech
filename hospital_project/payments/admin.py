from django.contrib import admin
from .models import payementsnew

class payfn(admin.ModelAdmin):
    list_display = ("Name", "consultationFee",)


admin.site.register(payementsnew, payfn)

# Register your models here.

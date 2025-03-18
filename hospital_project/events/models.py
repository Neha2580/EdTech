from django.db import models

# Create your models here.
class events(models.Model):
    eventname = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
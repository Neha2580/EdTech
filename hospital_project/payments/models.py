from django.db import models

class payments(models.Model):
    Name = models.CharField(max_length=255)
    Remarks = models.CharField(max_length=255)
    consultationFee = models.IntegerField(null=True)

class payementsnew(models.Model):
    Name = models.CharField(max_length=255)
    Remarks = models.CharField(max_length=255)
    consultationFee = models.IntegerField(null=True)


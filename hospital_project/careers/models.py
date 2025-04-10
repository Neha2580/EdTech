from django.db import models

# Create your models here.
class positions(models.Model):
    positionname = models.CharField(max_length=255)
    recrutingManager = models.CharField(max_length=255)
    hiringManager = models.CharField(max_length=255)
    openingDate = models.DateField(null=True)
    closedDate = models.DateField(null=True)
    notes = models.CharField(max_length=255)
    status = models.IntegerField(null=True)
    department = models.CharField(max_length=255)
    baseSalary = models.IntegerField(null= True)
    result = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.positionname} {self.baseSalary} {self.department}"
    
    
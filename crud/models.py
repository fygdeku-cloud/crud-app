from django.db import models

class Parcels(models.Model):
    name=models.CharField(max_length=50);
    surname=models.CharField(max_length=50);
    activity=models.CharField(max_length=20) 
    status=models.IntegerField(default=0)  
    
    def __str__(self):
        return f" le  colis de {self.name} "       
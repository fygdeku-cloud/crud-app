from django.utils import timezone
import random

from django.db import models

class Parcels(models.Model):
    tracking_number=models.CharField(max_length=15,unique=True)
    title=models.CharField(max_length=50);
    description=models.TextField(max_length=250);
    status=models.IntegerField(default=0)  
    date=models.DateTimeField(default=timezone.now)
    
    def save(self,*args,**kwargs):
        if not self.tracking_number:
            self.tracking_number='FR' + str(random.randint(111, 999))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f" Nom Colis: {self.title} de {self.description} "       
    
    
class User(models.Model):
    name=models.CharField(max_length=50);
    surname=models.CharField(max_length=250);
    age=models.IntegerField(default=0) 
    email=models.EmailField(unique=True) 
    
    def __str__(self):
        return f"M. {self.name} "       
    
    
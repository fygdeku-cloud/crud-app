from django.utils import timezone
import random
from django.contrib.auth.models import AbstractUser, User,AbstractBaseUser
from django.db import models

    
class User(AbstractUser):
    tracking_number_user=models.CharField(max_length=15,unique=True,null=True,blank=True)
    pass
    
    def __str__(self):
        return f"M. {self.username} "  
    
    def save(self,*args,**kwargs):
        if not self.tracking_number_user:
          self.tracking_number_user='FR' + str(random.randint(100, 999))
        super().save(*args, **kwargs)     
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Profil de {self.user.name}" 
    
    
class Parcels(models.Model):
    tracking_number=models.CharField(max_length=15,unique=True)
    title=models.CharField(max_length=50);
    description=models.TextField(max_length=250);
    status=models.IntegerField(default=0)  
    date=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='parcels')
    
    def save(self,*args,**kwargs):
        if not self.tracking_number:
            self.tracking_number='FR' + str(random.randint(111, 999))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f" Nom Colis: {self.title} de {self.description} "       
    
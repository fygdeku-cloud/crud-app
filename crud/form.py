from django import forms
from .models import Parcels,User

class RegisterParcelForm(forms.ModelForm):
   class Meta:
      model=Parcels
      fields=['title','description','date'] 
      widgets={
         'date':forms.HiddenInput()
      }  
      
      
class LoginForm(forms.ModelForm):
      password=forms.CharField(widget=forms.PasswordInput)
      class Meta:
         model=User
         fields=['username','email','password'] 
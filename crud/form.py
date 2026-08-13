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
      class Meta:
         model=User
         fields=['name','surname','email','password'] 
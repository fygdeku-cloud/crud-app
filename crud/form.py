from django import forms
from .models import Parcels,Client

class RegisterParcelForm(forms.ModelForm):
   class Meta:
      model=Parcels
      fields=['title','description','date'] 
      widgets={
         'date':forms.HiddenInput()
      }  
      
      
class LoginForm(forms.ModelForm):
      class Meta:
         model=Client
         fields=['name','surname','email','password'] 
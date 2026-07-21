from django import forms
from .models import Parcels

class RegisterParcelForm(forms.ModelForm):
   class Meta:
      model=Parcels
      fields=['name','surname','activity']   
from django import forms

class addForm(forms.ModelForm):
    name=forms.CharField(max_length=50,placeholder="Votre nom");
    surname=forms.CharField(max_length=50,placeholder="Votre nom");
    age=forms.IntegerField(max_digit=10,placeholder="Votre nom");
    comment=forms.DateField(required=True);
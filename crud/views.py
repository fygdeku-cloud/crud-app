from django.shortcuts import render
from django.http import HttpResponse
from .form import RegisterParcelForm
from .models import Parcels

def home_page(request):
    nb_colis=len(Parcels.objects.all())
    return render(request,'index.html' ,context={'nb_colis':nb_colis})

def parcels_page(request):
    return render(request, "parcels.html" ,context={'colis':Parcels.objects.all()})


def add_parcel_page(request):
    if request.method == 'POST':
        form=RegisterParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"parcels.html", context={'colis':Parcels.objects.all()})
    else:
        form=RegisterParcelForm()
        return render(request,"add_parcels_page.html", context={'form':form})
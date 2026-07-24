from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .form import RegisterParcelForm,LoginForm
from .models import Parcels,User
from django.utils.translation import gettext as _

def login_page(request):
    nb_colis=len(Parcels.objects.all())
    if request.method == 'POST':
       form=LoginForm(request.POST)
       if form.is_valid():
           user=form.save()
           return render(request,"home.html", context={'nb_colis':nb_colis,'name':user.name})
    else:
       form=LoginForm()
    return render(request,'index.html', context={'form':form,'nb_colis':nb_colis })
    


def home_page(request):
    nb_colis=len(Parcels.objects.all())
    return render(request,'home.html' ,context={'nb_colis':nb_colis})

def parcels_page(request):
    message = _("Votre commande a été validée.")
    return render(request, "parcels.html" ,context={'colis':Parcels.objects.all()})


def tracking_page(request):
    parcel=None
    error=None
    if request.method == 'POST':
       tracking_number=request.POST.get('tracking_number')
       try:
           parcel=Parcels.objects.get(tracking_number=tracking_number)
       except Parcels.DoesNotExist:
           error="Aucun colis n'existe avec ce suivi"
    return render(request,"tracking.html",context={'parcel':parcel, 'error':error})       


def add_parcel_page(request):
    if request.method == 'POST':
        form=RegisterParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"parcels.html", context={'colis':Parcels.objects.all()})
    else:
        form=RegisterParcelForm()
        return render(request,"add_parcels_page.html", context={'form':form})
    
def delete_parcel_page(request,parcel_id):
    parcel=get_object_or_404(Parcels, id=parcel_id)
    parcel.delete()
    return redirect('/parcels/')
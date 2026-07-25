from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .form import RegisterParcelForm,LoginForm
from .models import Parcels,User
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from .tasks import envoyer_email_bienvenue


def login_page(request):
    nb_colis = Parcels.objects.count()  
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_name'] = user.name
            email_user = user.email  
            envoyer_email_bienvenue.delay(email_user)
            return redirect('home_page') 
    else:
        form = LoginForm()
    return render(request, 'index.html', context={'form': form, 'nb_colis': nb_colis})

def home_page(request):
    nb_colis=Parcels.objects.count()
    user_name = request.session.get('user_name', '')
    return render(request, 'home.html', context={'nb_colis': nb_colis, 'name': user_name})

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

def erreur_404(request, exception):
    # La vue 404 accepte l'argument 'exception'
    return render(request, '404.html', status=404)

def erreur_500(request):
    # La vue 500 n'a pas besoin de l'argument 'exception'
    return render(request, '500.html', status=500)
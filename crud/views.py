from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request,'index.html')

def parcels_page(request):
    return render(request, "parcels.html")
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import BusquedaForm
from .scrapper import get_Links,get_Links_Details
from .models import MainWebs,DetailsWeb
from django.contrib.auth.models import User

def home_inicio(request):
    form = BusquedaForm()
    if request.method == "POST":
        form_ = BusquedaForm(request.POST)
        if form_.is_valid():
            url = form_.cleaned_data["url_a_buscar"]
            MainWebs.objects.create(url = url)                 
        return render(request,'principal.html',{"form":form,"resultado":MainWebs.objects.all()})
    return render(request,'principal.html',{"form":form})

def home_detalles(request):
    return render(request,'detalles.html',{})

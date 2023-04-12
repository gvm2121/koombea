from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .forms import BusquedaForm
from .models import MainWebs,DetailsWeb
from .tasks import get_Links
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home_inicio(request):
    form = BusquedaForm()
    if request.method == "POST":
        form_ = BusquedaForm(request.POST)
        if form_.is_valid():
            user = request.user
            url = form_.cleaned_data["url_a_buscar"]
            MainWebs.objects.create(url = url,user=user)
            #import pdb;pdb.set_trace()
            get_Links.delay(url,request.user.id)              
        return render(request,'principal.html',{"form":form,"resultado":MainWebs.objects.filter(user=request.user)})
    return render(request,'principal.html',{"form":form,"resultado":MainWebs.objects.filter(user=request.user)})

@login_required
def home_detalles(request,id):
    q = DetailsWeb.objects.filter(web_parent=MainWebs.objects.get(id=id,user=request.user))
    return render(request,'detalles.html',{"query":q})


def home_login(request):
    if request.method=="POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=email,password=password)
        if user is not None:
            login(request, user)
            return redirect("home_inicio")
        else:
            messages.add_message(request, messages.INFO, 'credenciales erróneas')
            return render(request,'login.html',{})
    return render(request,'login.html',{})

@login_required
def home_logout(request):
    logout(request)
    return render(request,'login.html',{})
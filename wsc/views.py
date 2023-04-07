from django.shortcuts import render
from .forms import BusquedaForm
from .models import MainWebs,DetailsWeb
from .tasks import get_Links

def home_inicio(request):
    form = BusquedaForm()
    if request.method == "POST":
        form_ = BusquedaForm(request.POST)
        if form_.is_valid():
            url = form_.cleaned_data["url_a_buscar"]
            MainWebs.objects.create(url = url)
            get_Links.delay(url)              
        return render(request,'principal.html',{"form":form,"resultado":MainWebs.objects.all()})
    return render(request,'principal.html',{"form":form,"resultado":MainWebs.objects.all()})

def home_detalles(request,id):
    q = DetailsWeb.objects.filter(web_parent=MainWebs.objects.get(id=id))
    return render(request,'detalles.html',{"query":q})

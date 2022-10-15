from django.shortcuts import render
from servicio.models import Servicio
#from .models import Servicio

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "servicio/Service.html", {"servicios": servicios})
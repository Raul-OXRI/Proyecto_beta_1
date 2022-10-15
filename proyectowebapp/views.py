from django.shortcuts import render, HttpResponse
from servicio.models import Servicio

#------------------------------------------------------------------------------------

def home(request):
    return render(request, "proyectowebapp/Home.html")

#------------------------------------------------------------------------------------

#def servicios(request):
#    servicios = Servicio.objects.all()
#    return render(request, "proyectowebapp/Service.html", {"servicios": servicios})
#------------------------------------------------------------------------------------

def tienda(request):
    return render(request, "proyectowebapp/Shop.html")

#------------------------------------------------------------------------------------

def blog(request):
    return render(request, "proyectowebapp/Blog.html")

#------------------------------------------------------------------------------------

def contacto(request):
    return render(request, "proyectowebapp/Contact.html")

#------------------------------------------------------------------------------------
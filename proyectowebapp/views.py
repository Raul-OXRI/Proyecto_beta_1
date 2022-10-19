from django.shortcuts import render, HttpResponse

#------------------------------------------------------------------------------------

def home(request):
    return render(request, "proyectowebapp/Home.html")

#------------------------------------------------------------------------------------

#def tienda(request):
#    return render(request, "proyectowebapp/Shop.html")

#------------------------------------------------------------------------------------

#def blog(request):
#    return render(request, "proyectowebapp/Blog.html")

#------------------------------------------------------------------------------------

#def contacto(request):
#    return render(request, "proyectowebapp/Contact.html")

#------------------------------------------------------------------------------------
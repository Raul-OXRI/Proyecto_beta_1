from django.shortcuts import render
from .forms import FormularioContacto

#------------------------------------------------------------------------------------

def contacto(request):
    formulario_contacto = FormularioContacto()
    return render(request, "contacto/Contact.html", {'miFormulario': formulario_contacto})

#------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------
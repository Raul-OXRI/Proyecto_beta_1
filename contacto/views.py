from django.shortcuts import redirect, render, HttpResponse
from .forms import FormularioContacto
from django.core.mail import EmailMessage
#------------------------------------------------------------------------------------

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":

        formulario_contacto = FormularioContacto(data = request.POST)

        if formulario_contacto.is_valid():

            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage(
                    subject = 'Realizando pruebas',
                    body = (contenido),
                    from_email = 'jose.botzoc.30@gmail.com',
                    to =[email],
                    reply_to = [email],)

            try:
                email.send()
                return redirect("/Contact/?valido")
            except:
                return redirect("/Contact/?novalido")
        
    return render(request, "contacto/Contact.html",{'miFormulario':formulario_contacto})

#------------------------------------------------------------------------------------
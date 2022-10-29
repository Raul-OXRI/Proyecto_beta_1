
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Service/', include("servicio.urls")),
    path('Blog/', include("blog.urls")),
    path('Shop/', include("tienda.urls")),
    path('Contact/', include("contacto.urls")),
    path('carro/', include("carro.urls")),
    path('autenticacion', include("auteticacion.urls")),
    path('pedidos/', include('pedidos.urls')),
    path('', include("proyectowebapp.urls")),
    

]

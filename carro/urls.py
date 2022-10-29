from django.urls import path
from carro import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "carro"

#---------------------------------------------------------------------------------------------------------------

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name = "agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name = "eliminar"),
    path("resta/<int:producto_id>/", views.resta_producto, name = "resta"),
    path("limpiar/", views.limpiar_producto, name = "limpiar"),
]

#---------------------------------------------------------------------------------------------------------------
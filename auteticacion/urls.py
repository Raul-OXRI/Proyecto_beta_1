from asyncio.log import logger
from django.urls import path
from .views import VRegistro, cerrar_session, logear

#------------------------------------------------------------------------------------

urlpatterns = [
    path('', VRegistro.as_view(), name = "Autenticacion"),
    path('cerrar_sesion', cerrar_session, name = "cerrar_sesion"),
    path('logear', logear , name = "logear"),
]

#------------------------------------------------------------------------------------

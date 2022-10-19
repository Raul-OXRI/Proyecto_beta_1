from django.urls import path
from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = "Home"),
    #path('Shop/', views.tienda, name = "Tienda"),
    #path('Blog/', views.blog, name = "Blog"),
    #path('Contact/', views.contacto, name = "Contacto"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

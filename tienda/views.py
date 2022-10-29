from django.shortcuts import render
from tienda.models import Producto,CategoriaProd

#------------------------------------------------------------------------------------

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda/Shop.html", {"productos": productos})

#------------------------------------------------------------------------------------


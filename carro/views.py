from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto =  Producto.objects.get(id = producto_id)
    carro.agregar(producto = producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto =  Producto.objects.get(id = producto_id)
    carro.eliminar(producto = producto)
    return redirect("Tienda")

def resta_producto(request, producto_id):
    carro = Carro(request)
    producto =  Producto.objects.get(id = producto_id)
    carro.resta_producto(producto = producto)
    return redirect("Tienda")

def limpiar_producto(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")


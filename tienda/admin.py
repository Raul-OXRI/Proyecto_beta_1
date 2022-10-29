from django.contrib import admin
from .models import CategoriaProd, Producto


class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(CategoriaProd, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
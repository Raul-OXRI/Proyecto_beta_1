from statistics import linear_regression
from django.contrib import admin
from .models import Pedido, LineaPedido

admin.site.register([Pedido, LineaPedido])
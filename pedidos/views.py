from django.shortcuts import render
from .models import Pedido
from django.utils import timezone

def pedidos_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedidos_list.html', {'pedidos': pedidos})

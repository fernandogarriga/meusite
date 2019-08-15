from django.shortcuts import render

def pedidos_list(request):
    return render(request, 'pedidos/pedidos_list.html', {})

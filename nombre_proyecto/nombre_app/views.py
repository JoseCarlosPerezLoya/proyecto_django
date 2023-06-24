from django.shortcuts import render
from .models import Productos
from .forms import ProductoForm

def productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def ingresar_producto(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Realizar acciones adicionales si es necesario
    return render(request, 'ingresar_producto.html', {'form': form})

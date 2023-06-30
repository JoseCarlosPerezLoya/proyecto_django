from django.shortcuts import render
from .models import Productos
from .forms import ProductoForm

def productos(request):
    productos = Productos.objects.all()
    productos_var = 'productos.html'
    print(productos_var)
    return render(request, productos_var, {'productos': productos})

def ingresar_producto(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save() 
        return render(request, 'ingresar_producto.html', {'form': form})        ##    en el regreso regresar otro htpml
    else:
        form = ProductoForm()
        return render(request, 'ingresar_producto.html', {'form': form}) 


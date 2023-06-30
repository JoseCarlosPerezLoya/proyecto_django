from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('agregar', views.ingresar_producto, name='agregar'),
]

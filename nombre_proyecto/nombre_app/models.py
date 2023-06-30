from django.db import models

class Productos(models.Model):
   
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_registro = models.DateField(auto_now_add=False)
    estatus = models.BooleanField(default=True)


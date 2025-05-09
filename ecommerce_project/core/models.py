from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True, default='TEMP')
    nombre = models.CharField(max_length=100, default='Producto sin nombre')
    descripcion = models.TextField(blank=True, default='Sin descripción')
    marca = models.CharField(max_length=50, default='Sin marca')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, default='default.jpg')

    def __str__(self):
        return self.nombre


    def __str__(self):
        return self.nombre
    
    #creacion del modelo para los productos en la rubrica junto a sus parametros, se le da un valor no nulo para hacer andar el programa antes de
    #crear una base de datos para esta
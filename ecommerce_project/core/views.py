from django.shortcuts import render
from rest_framework import generics,filters
from .models import Producto
from .serializers import ProductoSerializer

def index(request):
    productos = [
        {'nombre': 'Martillo', 'precio': 7990, 'imagen': 'images/martillo.jpg'},
        {'nombre': 'Destornillador', 'precio': 4990, 'imagen': 'images/destornillador.jpg'},
        {'nombre': 'Serrucho', 'precio': 10990, 'imagen': 'images/serrucho.jpg'},
    ]
    return render(request, 'index.html', {'productos': productos})

def pago(request):
    return render(request, 'pago.html')

class ProductoListAPIView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'descripcion', 'marca']

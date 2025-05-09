from django.urls import path
from .views import ProductoListAPIView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pago/', views.pago, name='pago'),
    path('api/productos/', ProductoListAPIView.as_view(), name='api_productos'),
]




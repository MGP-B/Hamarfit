from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('sucursales/',views.sucursales, name='sucursales'),
    path('checkout/',views.checkout, name='checkout'),
]
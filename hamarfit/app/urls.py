from django.urls import path, include
from . import views

urlpatterns = [
    # Index
    path('',views.index, name='index'),

    # Apartado de 'user'
    path('sucursales/',views.sucursales_user, name='user/sucursales'),
    path('checkout/',views.checkout, name='user/checkout'),
    path('ajustes_cuenta/',views.ajustes_cuenta, name='user/ajustes_cuenta'),
    path('metodo_pago/',views.metodo_pago, name='user/metodo_pago'),
    path('planes_contratados/',views.planes_contratados, name='user/planes_contratados'),
    path('registro/',views.registro, name='user/registro'),


    # Apartado de 'admin'
    path('admin/clientes/',views.clientes, name='admin/clientes'),
    path('admin/configuracion/',views.configuracion, name='admin/configuracion'),
    path('admin/dashboard/',views.dashboard, name='admin/dashboard'),
    path('admin/finanzas/',views.finanzas, name='admin/finanzas'),
    path('admin/login/',views.login, name='admin/login'),
    path('admin/sucursales/',views.sucursales_admin, name='admin/sucursales'),
]
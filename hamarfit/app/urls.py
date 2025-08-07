from django.urls import path, include
from . import views

urlpatterns = [
    # ----- Index -----
    path('',views.index, name='index'),

    # ----- Apartado de 'user' -----
    path('sucursales/',views.sucursales_user, name='user/sucursales'),
    path('checkout/',views.checkout, name='user/checkout'),
    path('ajustes_cuenta/',views.ajustes_cuenta, name='user/ajustes_cuenta'),
    path('metodo_pago/',views.metodo_pago, name='user/metodo_pago'),
    path('planes_contratados/',views.planes_contratados, name='user/planes_contratados'),
    path('registro/',views.registro, name='user/registro'),
    path('inicio_user/',views.proteger_vista, name='inicio_user'),
    path('logout_user/',views.logout_user, name='logout_user'),


    # ----- Apartado de 'admin' -----
    path('admin/clientes/',views.clientes, name='admin/clientes'),
    path('admin/configuracion/',views.configuracion, name='admin/configuracion'),
    path('admin/',views.dashboard, name='admin/'),
    path('admin/inscripciones_renovaciones/',views.inscripciones_renovaciones, name='admin/inscripciones_renovaciones'),
    path('admin/login/',views.login, name='admin/login'),
    path('admin/sucursales/',views.sucursales_admin, name='admin/sucursales'),


    # ----- Desplegables de 'admin' -----
    # Clientes
    path('admin/clientes/detalles_cliente/', views.detalles_cliente, name= 'admin/clientes/detalles_cliente/'),
    path('admin/clientes/registrar_cliente/', views.registrar_cliente, name='admin/clientes/registrar_cliente/'),
    path('admin/clientes/seleccionar_plan/', views.seleccionar_plan, name='admin/clientes/seleccionar_plan/'),

    # Configuración
    path('admin/configuracion/editar_usuario/', views.editar_usuario, name='admin/configuracion/editar_usuario/'),
    path('admin/configuracion/registrar_usuario/', views.registrar_usuario, name='admin/configuracion/registrar_usuario/'),

    # inscripciones_renovaciones
    path('admin/inscripciones_renovaciones/registrar_renovacion/', views.registrar_renovacion, name='admin/inscripciones_renovaciones/registrar_renovacion/'),
    path('admin/inscripciones_renovaciones/detalles_factura/', views.detalles_factura, name='admin/inscripciones_renovaciones/detalles_factura/' ),

    # Sucursales
    path('admin/sucursales/registrar_sucursal/',views.registrar_sucursal, name='admin/sucursales/registrar_sucursal/'),
    path('admin/sucursales/editar_sucursal/', views.editar_sucursal, name='admin/sucursales/editar_sucursal/')
]
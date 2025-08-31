from django.urls import path, include
from . import views

urlpatterns = [
    # ----- Index -----
    path('',views.index, name='index'),

    # ----- Apartado de 'user' -----
    path('ajustes_cuenta/',views.ajustes_cuenta, name='user/ajustes_cuenta'),
    path('planes_contratados/',views.planes_contratados, name='user/planes_contratados'),
    path('inicio_user/',views.inicio_user, name='inicio_user'),
    path('logout_user/',views.logout_user, name='logout_user'),
    path('ajustes_cuenta/cambiar_contrasena/', views.cambiar_contrasena, name='user/ajustes_cuenta/cambiar_contrasena'),


    # ----- Apartado de 'admin' -----
    path('admin/clientes/',views.clientes, name='admin/clientes'),
    path('admin/configuracion/',views.configuracion, name='admin/configuracion'),
    path('admin/',views.dashboard, name='admin/'),
    path('admin/inscripciones_renovaciones/',views.inscripciones_renovaciones, name='admin/inscripciones_renovaciones'),
    path('admin/login/',views.login, name='admin/login'),
    path('admin/sucursales/',views.sucursales_admin, name='admin/sucursales'),


    # ----- Desplegables de 'admin' -----
    # Clientes
    path('admin/clientes/detalles_cliente/<int:id>', views.detalles_cliente, name= 'admin/clientes/detalles_cliente/'),
    path('admin/clientes/eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('admin/clientes/registrar_cliente/', views.registrar_cliente, name='admin/clientes/registrar_cliente/'),
    path('admin/clientes/seleccionar_plan/', views.seleccionar_plan, name='admin/clientes/seleccionar_plan/'),

    # Configuración
    path('admin/configuracion/detalles_usuario/<int:id>', views.detalles_usuario, name='admin/configuracion/detalles_usuario/'),
    path('admin/configuracion/registrar_usuario/', views.registrar_usuario, name='admin/configuracion/registrar_usuario/'),
    path('admin/configuracion/reasignar_inscripciones/<int:id_empleado>/', views.reasignar_inscripciones, name='reasignar_inscripciones'),
    path('admin/configuracion/ejecutar_reasignacion/', views.ejecutar_reasignacion, name='ejecutar_reasignacion'),

    # inscripciones_renovaciones
    path('admin/inscripciones_renovaciones/registrar_renovacion/', views.registrar_renovacion, name='admin/inscripciones_renovaciones/registrar_renovacion/'),
    path('admin/inscripciones_renovaciones/detalles_factura/<int:id>', views.detalles_factura, name='admin/inscripciones_renovaciones/detalles_factura/' ),

    # Sucursales
    path('admin/sucursales/registrar_sucursal/', views.registrar_sucursal, name='registrar_sucursal'),
    path('admin/sucursales/editar_sucursal/', views.editar_sucursal, name='editar_sucursal'),

]

# Pillow
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
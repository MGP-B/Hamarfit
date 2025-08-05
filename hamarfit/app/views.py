from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
# def index(req):
#     return HttpResponse('Bienvenido a HAMARFIT')

# Index
def index(req):
    return render(req,'index.html')

#  ----- Paginas del apartado de 'user' -----
def sucursales_user(req):
    return render(req,'user_pages/sucursales.html')

def checkout(req):
    return render(req,'user_pages/checkout.html')

def ajustes_cuenta(req):
    return render(req, 'user_pages/ajustes-de-cuenta.html')

def metodo_pago(req):
    return render(req, 'user_pages/metodo_pago.html')

def planes_contratados(req):
    return render(req, 'user_pages/planes-contratados.html')

def registro(req):
    return render(req, 'user_pages/registro.html')



# ----- Paginas del apartado de 'admin' -----
def clientes(req):
    clientes = Clientes.objects.all()
    return render(req, 'admin_pages/clientes.html', {'clientes': clientes})

def configuracion(req):
    return render(req, 'admin_pages/configuracion.html')

def dashboard(req):
    return render(req, 'admin_pages/dashboard.html')

def finanzas(req):
    return render(req, 'admin_pages/finanzas.html')

def login(req):
    return render(req, 'admin_pages/login.html')

def sucursales_admin(req):
    return render(req, 'admin_pages/sucursales.html')



# ----- Desplegables de 'admin' -----
# Clientes
def detalles_cliente(req):
    return render(req, 'admin_pages/desplegables/clientes/detalles_del_cliente.html')

def registrar_cliente(req):
    if req.method == 'POST':
        print('no funciona')
        form = ClientesForm(req.POST)
        if form.is_valid():
            form.save()
            # Redirige o muestra mensaje de éxito
            return redirect('admin/clientes/')
        else:
            # Si el formulario no es válido, vuelve a mostrar el formulario con errores
            
            return redirect('../')
    else:
        form = ClientesForm()
        return render(req, 'admin_pages/desplegables/clientes/registrar_nuevo_cliente.html', {'form': form})

def seleccionar_plan(req):
    return render(req, 'admin_pages/desplegables/clientes/seleccionar_plan.html')


# Configuración
def editar_usuario(req):
    return render(req, 'admin_pages/desplegables/configuracion/editar_usuario.html')

def registrar_usuario(req):
    return render(req, 'admin_pages/desplegables/configuracion/nuevo_usuario.html')


# Finanzas
def registrar_transaccion(req):
    return render(req, 'admin_pages/desplegables/finanzas/registrar_transaccion.html')

def detalles_factura(req):
    return render(req, 'admin_pages/desplegables/finanzas/detalles_de_factura.html')


# Sucursales
def registrar_sucursal(req):
    return render(req, 'admin_pages/desplegables/sucursales/agregar_sucursal.html')

def editar_sucursal(req):
    return render(req, 'admin_pages/desplegables/sucursales/editar_sucursal.html')


# ----- Paginas de error -----
# def error_404(req, exception):
#     return render(req, 'error_pages/404.html', status=404)
# def error_500(req):
#     return render(req, 'error_pages/500.html', status=500)


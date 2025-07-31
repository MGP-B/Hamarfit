from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from . models import *
# from django.urls import reverse

# Create your views here.
# def index(req):
#     return HttpResponse('Bienvenido a HAMARFIT')

# Index
def index(req):
    return render(req,'index.html')

#  ----- Paginas del apartado de 'user' -----
# def sucursales_user(req):
#     return render(req,'user_pages/sucursales.html')

def sucursales_user(req):
    # Obtiene el ID del plan desde la URL (ej. ?id_plan=2)
    id_plan = req.GET.get('id_plan')
    # Busca el objeto Planes con ese ID en la base de datos
    plan = Planes.objects.get(id_plan=id_plan)
    # Obtiene todas las sucursales disponibles
    sucursales = Sucursales.objects.all()
    # Renderiza la plantilla 'sucursales.html' y le pasa el plan y las sucursales
    return render(req, 'user_pages/sucursales.html', {'plan': plan, 'sucursales': sucursales})

def checkout(req):
    return render(req,'user_pages/checkout.html')

def ajustes_cuenta(req):
    return render(req, 'user_pages/ajustes-de-cuenta.html')

def metodo_pago(req):
    return render(req, 'user_pages/metodo_pago.html')

def planes_contratados(req):
    return render(req, 'user_pages/planes-contratados.html')

def registro(req):
    # Obtiene el ID del plan y la sucursal desde la URL (ej. ?id_plan=2&id_sucursal=1)
    id_plan = req.GET.get('id_plan')
    id_sucursal = req.GET.get('id_sucursal')

    # Si falta alguno de los dos, redirige al selector de sucursales
    if not id_plan or not id_sucursal:
        return redirect('user/sucursales')

    # Busca el plan y la sucursal en la base de datos, o lanza error 404 si no existen
    plan = get_object_or_404(Planes, id_plan=id_plan)
    sucursal = get_object_or_404(Sucursales, id_sucursal=id_sucursal)

    # Si el usuario envió el formulario (método POST)
    if req.method == 'POST':
        # Crea el formulario con los datos enviados
        form = ClientesForm(req.POST)

        # Si el formulario es válido
        if form.is_valid():
            # Crea el cliente sin guardarlo aún en la base de datos
            cliente = form.save(commit=False)

            # Asigna el plan, la sucursal y el estado manualmente
            cliente.id_plan = plan
            cliente.id_sucursal = sucursal
            cliente.id_estado = Estados.objects.get(id_estado=1)
            # print(cliente.__dict__)

            # Guarda el cliente en la base de datos
            cliente.save()

            # Redirige al login del admin después del registro exitoso
            return redirect('../')
        
        # Si el formulario no es válido, podrías imprimir los errores (comentado)
        # else:
        #     print(form.errors)
    else:
        # Si es una petición GET, muestra el formulario vacío
        form = ClientesForm()

    # Renderiza la plantilla 'registro.html' con el formulario y los datos del plan y sucursal
    return render(req, 'user_pages/registro.html', {'form': form, 'plan': plan, 'sucursal': sucursal})



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
        form = ClientesForm(req.POST)
        if form.is_valid():
            form.save()
            # Redirige o muestra mensaje de éxito
            return redirect('../')
        else:
            # Si el formulario no es válido, vuelve a mostrar el formulario con errores
            return render(req, 'admin_pages/desplegables/clientes/registrar_nuevo_cliente.html', {'form': form})
    else:
        form = ClientesForm()
        return render(req, 'admin_pages/desplegables/clientes/registrar_nuevo_cliente.html', {'form': form})

def seleccionar_plan(req):
    return render(req, 'admin_pages/desplegables/clientes/seleccionar_plan.html')


# Configuración
def editar_usuario(req):
    return render(req, 'admin_pages/desplegables/configuracion/editar_usuario.html')

def registrar_usuario(req):
    if req.method == 'POST':
        form = EmpleadosForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            return render(req, 'admin_pages/desplegables/configuracion/nuevo_usuario.html')
        
    else:
        form = EmpleadosForm()
    return render(req, 'admin_pages/desplegables/configuracion/nuevo_usuario.html', {'form': form})


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


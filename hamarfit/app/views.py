from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from . models import *
from datetime import date
from django.views.decorators.cache import never_cache
from .decorators import cliente_required, empleado_required
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
    return render(req, 'user_pages/sucursales.html')

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
@empleado_required
def clientes(req):
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)
    clientes = Clientes.objects.all()
    return render(req, 'admin_pages/clientes.html', {'clientes': clientes, 'empleado': empleado})

@empleado_required
def configuracion(req):
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)
    empleados = Empleados.objects.all()
    return render(req, 'admin_pages/configuracion.html', {'empleados':empleados, 'empleado': empleado})

@empleado_required
@never_cache
def dashboard(req):
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)
    renovaciones = InscripcionesRenovaciones.objects.filter(descripcion = 'Renovación')
    inscripciones = InscripcionesRenovaciones.objects.filter(descripcion = 'Inscripción')
    return render(req, 'admin_pages/dashboard.html', {
        'renovaciones': renovaciones, 
        'inscripciones': inscripciones
        })

    return render(req, 'admin_pages/dashboard.html', {'empleado': empleado})

@empleado_required
def inscripciones_renovaciones(req):
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)
    return render(req, 'admin_pages/inscripciones_renovaciones.html', {'empleado': empleado})

# def login(req):
#     if req.method == 'POST':
#         correo = req.POST.get('correo_cliente')
#         contrasena = req.POST.get('contrasena_cliente')

#         try:
#             cliente = Clientes.objects.get(correo_cliente=correo, contrasena_cliente=contrasena)
#             req.session['cliente_id'] = cliente.id_cliente
#             return redirect('inicio_user')
#         except Clientes.DoesNotExist:
#             error = "Correo o contraseña incorrectos."
#             return render(req, 'admin_pages/login.html', {'error': error})
#     return render(req, 'admin_pages/login.html')
    # inscripciones_renovaciones = InscripcionesRenovaciones.objects.all()
    # return render(req, 'admin_pages/inscripciones_renovaciones.html', {'inscripciones_renovaciones':inscripciones_renovaciones})

def login(req):
    if req.method == 'POST':
            correo = req.POST.get('correo')
            contrasena = req.POST.get('contrasena')

            # Verificar si es un empleado
            try:
                empleado = Empleados.objects.select_related('id_rol').get(correo_empleado=correo, contrasena_empleado=contrasena)
                req.session['empleado_id'] = empleado.id_empleado
                req.session['rol'] = empleado.id_rol.rol
                return redirect('admin/') # Dashboard para empleados
            except Empleados.DoesNotExist:
                pass # Si no es empleado, sigue con cliente

            # Verificar si es cliente
            try:
                cliente = Clientes.objects.get(correo_cliente=correo, contrasena_cliente=contrasena)
                req.session['cliente_id'] = cliente.id_cliente
                return redirect('inicio_user')
            except Clientes.DoesNotExist:
                error = "Correo o contraseña incorrectos."
                return render(req, 'admin_pages/login.html', {'error': error})
            
    return render(req, 'admin_pages/login.html')

@cliente_required
@never_cache
def inicio_user(req):
    return render(req, 'user_pages/inicio_user.html')



# @never_cache
# def proteger_vista(req):
#     if not req.session.get('cliente_id'):
#         return redirect('admin/login')
    
#     return render(req, 'user_pages/inicio_user.html')

def logout_user(req):
    req.session.flush()
    return redirect('index')


@empleado_required
def sucursales_admin(req):
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)
    sucursales = Sucursales.objects.all()
    return render(req, 'admin_pages/sucursales.html', {'sucursales': sucursales, 'empleado': empleado})



# ----- Desplegables de 'admin' -----
# Clientes
def detalles_cliente(req):
    return render(req, 'admin_pages/desplegables/clientes/detalles_del_cliente.html')

def registrar_cliente(req):
    if req.method == 'POST':
        form = anadirCliente(req.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            print("[DEBUG] Errores del formulario:", form.errors)
    else:
        form = anadirCliente()
    sucursales = Sucursales.objects.all()
    return render(req, 'admin_pages/desplegables/clientes/registrar_nuevo_cliente.html', {'form': form, 'sucursales': sucursales})


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
            print('Los errores del formulario son: ', form.errors)
    else:
        form = EmpleadosForm()

    sucursales = Sucursales.objects.all()
    return render(req, 'admin_pages/desplegables/configuracion/nuevo_usuario.html', {'form': form,'sucursales': sucursales})


# inscripciones_renovaciones
def registrar_renovacion(req):
    if req.method == 'POST':
        form = RenovacionesForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('../')  # Redirige después de guardar
        else:
            print('Los errores del formulario son: ', form.errors)
    else:
        form = RenovacionesForm()

    planes = Planes.objects.all()
    metodos_pago = MetodosPagos.objects.all()
    
    return render(req, 'admin_pages/desplegables/inscripciones_renovaciones/registrar_renovacion.html', {
        'form': form,
        'planes': planes,
        'metodos_pago': metodos_pago
        })


def detalles_factura(req):
    return render(req, 'admin_pages/desplegables/inscripciones_renovaciones/detalles_de_factura.html')


# Sucursales
def registrar_sucursal(req):
    if req.method == 'POST':
        form = SucursalesForm(req.POST, req.FILES)
        if form.is_valid():
            print("[DEBUG] Archivos recibidos:", req.FILES)
            form.save()
            return redirect('../')
        else:
            print("[DEBUG] Errores del formulario:", form.errors)
    else:
        form = SucursalesForm()
    return render(req, 'admin_pages/desplegables/sucursales/agregar_sucursal.html', {'form': form})


def editar_sucursal(req):
    return render(req, 'admin_pages/desplegables/sucursales/editar_sucursal.html')


# ----- Paginas de error -----
# def error_404(req, exception):
#     return render(req, 'error_pages/404.html', status=404)
# def error_500(req):
#     return render(req, 'error_pages/500.html', status=500)


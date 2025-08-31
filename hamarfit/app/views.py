from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from .forms import *
from . models import *
from datetime import date
from django.views.decorators.cache import never_cache
from .decorators import cliente_required, empleado_required, role_required
from django.db.models import Value
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models.functions import Concat  # Asegúrate de importar esto correctamente
from django.views.decorators.http import require_POST
# from django.urls import reverse

# Create your views here.
# def index(req):
#     return HttpResponse('Bienvenido a HAMARFIT')

# Index
def index(req):
    sucursales = Sucursales.objects.all()
    return render(req,'index.html', {'sucursales': sucursales})

#  ----- Paginas del apartado de 'user' -----
# def sucursales_user(req):
#     return render(req,'user_pages/sucursales.html')

def sucursales_user(req):
    return render(req, 'user_pages/sucursales.html')

def checkout(req):
    return render(req,'user_pages/checkout.html')

@cliente_required
@never_cache
def ajustes_cuenta(req):
    cliente_id = req.session.get('cliente_id')
    cliente = Clientes.objects.get(id_cliente=cliente_id)
    return render(req, 'user_pages/ajustes-de-cuenta.html', {'cliente': cliente})


@cliente_required
@never_cache
def planes_contratados(req):
    cliente_id = req.session.get('cliente_id')
    cliente = Clientes.objects.get(id_cliente=cliente_id)
    return render(req, 'user_pages/planes-contratados.html', {'cliente': cliente})
            

# ----- Paginas del apartado de 'admin' -----
@empleado_required
@role_required(['Admin', 'Gerente', 'Entrenador', 'Recepcionista'])
def clientes(req):
    query = req.GET.get('q', '').strip()
    if query:
        palabras = query.lower().split()
        clientes_qs = Clientes.objects.annotate(
            nombre_completo=Concat('nombre_cliente', Value(' '), 'apellido_cliente')
        )
        condiciones = Q()
        for palabra in palabras:
            condiciones |= Q(nombre_cliente__icontains=palabra)
            condiciones |= Q(apellido_cliente__icontains=palabra)
            condiciones |= Q(nombre_completo__icontains=palabra)
        resultados = clientes_qs.filter(condiciones)
    else:
        resultados = Clientes.objects.none()

    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)

    if query:
        clientes_qs = resultados
    else:
        clientes_qs = Clientes.objects.all()

    paginator = Paginator(clientes_qs, 10)  # 10 clientes por página
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(req, 'admin_pages/clientes.html', {
        'clientes': page_obj,
        'empleado': empleado,
        'resultados': resultados,
        'query': query,
        'page_obj': page_obj,
    })


@empleado_required
@role_required(['Admin', 'Gerente'])
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
    renovaciones = InscripcionesRenovaciones.objects.filter(descripcion = 'Renovación').order_by('-id_finanza')[:5]

    inscripciones = InscripcionesRenovaciones.objects.filter(descripcion = 'Inscripción').order_by('-id_finanza')[:5]
    return render(req, 'admin_pages/dashboard.html', {
        'renovaciones': renovaciones, 
        'inscripciones': inscripciones,
        'empleado': empleado
        })


@empleado_required
@role_required(['Admin', 'Gerente', 'Recepcionista'])
def inscripciones_renovaciones(req):
    # Barra de búsqueda
    query = req.GET.get('q', '').strip()

    # Solo si hay texto de búsqueda
    if query:
        # Normaliza el input
        palabras = query.lower().split()

        # Anota el nombre completo para búsquedas combinadas
        inscripciones = InscripcionesRenovaciones.objects.annotate(
            nombre_completo= Concat(
                'id_cliente__nombre_cliente',
                Value(' '),
                'id_cliente__apellido_cliente'
            )
        )

        # Construye condiciones dinámicas
        condiciones = Q()
        for palabra in palabras:
            condiciones |= Q(id_cliente__nombre_cliente__icontains=palabra)
            condiciones |= Q(id_cliente__apellido_cliente__icontains=palabra)
            condiciones |= Q(nombre_completo__icontains=palabra)

        resultados = inscripciones.filter(condiciones)
    else:
        resultados = InscripcionesRenovaciones.objects.none()

    # Cuenta iniciada
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)
    
    # Mostrar los registros
    if query:
        inscripciones_renovaciones_qs = resultados
    else:
        inscripciones_renovaciones_qs = InscripcionesRenovaciones.objects.all()

    paginator = Paginator(inscripciones_renovaciones_qs, 10)  # 10 clientes por página
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(req, 'admin_pages/inscripciones_renovaciones.html', {
    'inscripciones_renovaciones': page_obj, 
    'empleado': empleado, 
    'resultados': resultados, 
    'query': query,
    'page_obj': page_obj,
    })


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
    cliente_id = req.session.get('cliente_id')
    cliente = Clientes.objects.get(id_cliente=cliente_id)
    return render(req, 'user_pages/inicio_user.html', {'cliente': cliente})


def logout_user(req):
    req.session.flush()
    return redirect('index')


@empleado_required
@role_required(['Admin', 'Gerente'])
def sucursales_admin(req):
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)
    sucursales = Sucursales.objects.all()
    return render(req, 'admin_pages/sucursales.html', {'sucursales': sucursales, 'empleado': empleado})

@cliente_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        nueva = request.POST.get('nueva')
        confirmar = request.POST.get('confirmar')

        if not nueva or not confirmar:
            return JsonResponse({'status': 'error', 'message': 'Campos vacíos.'})

        if nueva != confirmar:
            return JsonResponse({'status': 'error', 'message': 'Las contraseñas no coinciden.'})

        if len(nueva) < 8:
            return JsonResponse({'status': 'error', 'message': 'La contraseña debe tener al menos 8 caracteres.'})

        id_cliente = request.session.get('id_cliente')
        if not id_cliente:
            return JsonResponse({'status': 'error', 'message': 'Sesión inválida. Por favor inicia sesión nuevamente.'})

        try:
            cliente = Clientes.objects.get(id_cliente=id_cliente)
        except Clientes.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cliente no encontrado.'})

        cliente.contrasena_cliente = nueva  # ← Se guarda en texto plano
        cliente.save()

        return JsonResponse({'status': 'success', 'message': 'Contraseña actualizada correctamente.'})

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})

# ----- Desplegables de 'admin' -----
# Clientes
# def detalles_cliente(req, id):
#     cliente = get_object_or_404(Clientes, id_cliente = id)
#     nota_cliente = NotaClientes.objects.filter(id_cliente = id)

#     mostrar_nota = get_object_or_404(NotaClientes, id_cliente = id)
#     return render(req, 'admin_pages/desplegables/clientes/detalles_del_cliente.html', {'cliente': cliente, 'nota_cliente': nota_cliente, 'mostrar_nota': mostrar_nota})

def detalles_cliente(req, id):
    # Obtener el cliente (esto es igual para GET y POST)
    cliente = get_object_or_404(Clientes, id_cliente=id)
    
    # Inicializar el formulario, vacío para GET o con datos para POST
    form = NotaClientesForm(req.POST or None)

    if req.method == 'POST':
        if form.is_valid():
            # Procesar el formulario de agregar nota
            nota = form.save(commit=False)
            # Asignar el cliente a la nota antes de guardar
            nota.id_cliente = cliente
            nota.save()
            # Redirigir para evitar que se envíe el formulario de nuevo
            return redirect('../', id=id)
        else:
            # Imprimir errores del formulario para depurar
            print('Errores del formulario:', form.errors)

    # Lógica para manejar solicitudes GET
    try:
        nota_cliente = NotaClientes.objects.filter(id_cliente=id)
        mostrar_nota = True
    except NotaClientes.DoesNotExist:
        nota_cliente = None
        mostrar_nota = False

    contexto = {
        'cliente': cliente,
        'nota_cliente': nota_cliente,
        'mostrar_nota': mostrar_nota,
        'form': form
    }
    
    return render(req, 'admin_pages/desplegables/clientes/detalles_del_cliente.html', contexto)

@require_POST
def eliminar_cliente(req, id):
    empleado_id = req.session.get('empleado_id')
    empleado = get_object_or_404(Empleados, id_empleado=empleado_id)

    if empleado.id_rol.rol not in ['Admin', 'Recepcionista']:
        return HttpResponseForbidden("No tienes permiso para eliminar clientes.")

    cliente = get_object_or_404(Clientes, id_cliente=id)

    # Aquí podrías validar si el cliente tiene inscripciones activas
    cliente.delete()

    return JsonResponse({'success': True, 'message': 'Cliente eliminado correctamente.'})

@role_required(['Admin', 'Recepcionista'])
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
def detalles_usuario(req, id):
    empleado = Empleados.objects.get(id_empleado = id)
    return render(req, 'admin_pages/desplegables/configuracion/detalles_usuario.html', {'empleado' : empleado})


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
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)
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
        'metodos_pago': metodos_pago,
        'empleado': empleado
        })


def detalles_factura(req, id):
    factura = InscripcionesRenovaciones.objects.get(id_finanza = id)

    return render(req, 'admin_pages/desplegables/inscripciones_renovaciones/detalles_de_factura.html', {'factura': factura})


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

def reasignar_inscripciones(request, id_empleado):
    empleado_origen = get_object_or_404(Empleados, pk=id_empleado)

    empleados_destino = Empleados.objects.exclude(pk=id_empleado) \
        .exclude(id_rol__rol='Entrenador')  # Excluye entrenadores

    return render(request, 'admin_pages/desplegables/configuracion/reasignar_inscripciones.html', {
        'empleado_origen': empleado_origen,
        'empleados_destino': empleados_destino
    })

def ejecutar_reasignacion(request):
    if request.method == 'POST':
        origen_id = request.POST.get('origen_id')
        destino_id = request.POST.get('destino_id')

        try:
            origen = Empleados.objects.get(pk=origen_id)
            destino = Empleados.objects.get(pk=destino_id)

            # Reasignar todas las inscripciones del empleado origen al destino
            InscripcionesRenovaciones.objects.filter(id_empleado=origen).update(id_empleado=destino)

            # Eliminar el empleado origen
            origen.delete()

            return JsonResponse({'success': True, 'message': 'Inscripciones reasignadas correctamente.'})
        except Empleados.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Empleado no encontrado.'}, status=404)
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)
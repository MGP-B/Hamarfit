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
import hashlib
# from django.urls import reverse


# Index
def index(req):
    sucursales = Sucursales.objects.all()
    return render(req,'index.html', {'sucursales': sucursales})


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
    try:
        renovacion = InscripcionesRenovaciones.objects.get(id_cliente = cliente_id, descripcion = 'Renovación')
        return render(req, 'user_pages/planes-contratados.html', {'cliente': cliente, 'renovacion': renovacion})
    except:
        return render(req, 'user_pages/planes-contratados.html', {'cliente': cliente})


# ----- Paginas del apartado de 'admin' -----
@empleado_required
@role_required(['Admin', 'Gerente', 'Entrenador', 'Recepcionista'])
def clientes(req):
    query = req.GET.get('q', '').strip()
    estado_id = req.GET.get('estado')
    plan_id = req.GET.get('plan')
    page_number = req.GET.get('page')

    # Base queryset con anotación
    clientes_qs = Clientes.objects.annotate(
        nombre_completo=Concat('nombre_cliente', Value(' '), 'apellido_cliente')
    )

    # Filtro por búsqueda textual
    if query:
        palabras = query.lower().split()
        condiciones = Q()
        for palabra in palabras:
            condiciones |= Q(nombre_cliente__icontains=palabra)
            condiciones |= Q(apellido_cliente__icontains=palabra)
            condiciones |= Q(nombre_completo__icontains=palabra)
        clientes_qs = clientes_qs.filter(condiciones)

    
    # Filtros por estado y plan
    if estado_id:
        clientes_qs = clientes_qs.filter(id_estado=estado_id)
    if plan_id:
        clientes_qs = clientes_qs.filter(id_plan=plan_id)

    # Paginación
    paginator = Paginator(clientes_qs, 10)
    page_obj = paginator.get_page(page_number)

    # Empleado desde sesión
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)

    return render(req, 'admin_pages/clientes.html', {
        'clientes': page_obj,
        'empleado': empleado,
        'query': query,
        'estado_id': estado_id,
        'plan_id': plan_id,
        'page_obj': page_obj,
        'estados': Estados.objects.all(),
        'planes': Planes.objects.all(),
    })


@empleado_required
@role_required(['Admin', 'Gerente'])
def configuracion(req):
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)
    empleados = Empleados.objects.exclude(id_empleado=empleado_id)
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
    query = req.GET.get('q', '').strip()
    plan_id = req.GET.get('plan')
    descripcion = req.GET.get('descripcion')
    page_number = req.GET.get('page')

    # Base queryset con anotación para nombre completo
    inscripciones_renovaciones_qs = InscripcionesRenovaciones.objects.annotate(
        nombre_completo=Concat(
            'id_cliente__nombre_cliente',
            Value(' '),
            'id_cliente__apellido_cliente'
        )
    )

    # Filtro por búsqueda textual
    if query:
        palabras = query.lower().split()
        condiciones = Q()
        for palabra in palabras:
            condiciones |= Q(id_cliente__nombre_cliente__icontains=palabra)
            condiciones |= Q(id_cliente__apellido_cliente__icontains=palabra)
            condiciones |= Q(nombre_completo__icontains=palabra)
        inscripciones_renovaciones_qs = inscripciones_renovaciones_qs.filter(condiciones)

    # Filtro por descripción
    if descripcion:
        inscripciones_renovaciones_qs = inscripciones_renovaciones_qs.filter(descripcion__icontains=descripcion)

    # Filtro por plan
    if plan_id:
        inscripciones_renovaciones_qs = inscripciones_renovaciones_qs.filter(id_plan_id=plan_id)

    # Paginación
    paginator = Paginator(inscripciones_renovaciones_qs, 10)
    page_obj = paginator.get_page(page_number)

    # Empleado desde sesión
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)

    # Lista de descripciones únicas para el select
    descripciones = InscripcionesRenovaciones.objects.values_list('descripcion', flat=True).distinct()

    return render(req, 'admin_pages/inscripciones_renovaciones.html', {
        'inscripciones_renovaciones': page_obj,
        'empleado': empleado,
        'query': query,
        'plan_id': plan_id,
        'descripcion': descripcion,
        'page_obj': page_obj,
        'descripciones': descripciones,
        'planes': Planes.objects.all(),
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

    sucursales = Sucursales.objects.all()
    return render(req, 'user_pages/inicio_user.html', {'cliente': cliente, 'sucursales': sucursales})


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

def detalles_cliente(req, id):
    # Obtener el cliente
    cliente = get_object_or_404(Clientes, id_cliente=id)
    sucursal_cliente = cliente.id_sucursal
    # Inicializar el formulario, vacío para GET o con datos para POST
    form = NotaClientesForm(req.POST or None)

    if req.method == 'POST':
        form_type = req.POST.get('form_type')

        if form_type == 'nota':
            form = NotaClientesForm(req.POST)
            if form.is_valid():
                nota = form.save(commit=False)
                nota.id_cliente = cliente
                nota.save()
                return redirect('../', id=id)
            else:
                print('Errores del formulario:', form.errors)

        elif form_type == 'entrenador':
            id_empleado = req.POST.get('id_empleado')
            if id_empleado:
                entrenador_cliente = EntrenadorCliente.objects.filter(id_cliente=cliente).first()
                if entrenador_cliente:
                    entrenador_cliente.id_empleado_id = id_empleado
                    entrenador_cliente.save()
                else:
                    EntrenadorCliente.objects.create(
                        id_cliente=cliente,
                        id_empleado_id=id_empleado
                    )
                return redirect('../', id=id)


    # Lógica para manejar solicitudes GET
    try:
        nota_cliente = NotaClientes.objects.filter(id_cliente=id)
        mostrar_nota = True
    except NotaClientes.DoesNotExist:
        nota_cliente = None
        mostrar_nota = False
    
    try:
        entrenador_cliente = EntrenadorCliente.objects.get(id_cliente = id)
    except:
        entrenador_cliente = None
        
    entrenadores = Empleados.objects.filter(id_rol = 3, id_sucursal = sucursal_cliente)
    entrenador_cliente = EntrenadorCliente.objects.filter(id_cliente=cliente).first()

    return render(req, 'admin_pages/desplegables/clientes/detalles_del_cliente.html', {
        'cliente': cliente,
        'nota_cliente': nota_cliente,
        'mostrar_nota': mostrar_nota,
        'form': form,
        'entrenadores': entrenadores,
        'entrenador_cliente': entrenador_cliente,
    })

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

    return render(req, 'admin_pages/desplegables/clientes/registrar_nuevo_cliente.html', {
        'form': form, 
        'sucursales': sucursales,
        })


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
    id_cliente = req.POST.get('id_cliente')
    empleado_id = req.session.get('empleado_id')
    empleado = Empleados.objects.get(id_empleado=empleado_id)

    planes = Planes.objects.all()
    metodos_pago = MetodosPagos.objects.all()

    if req.method == 'POST':
        form = RenovacionesForm(req.POST)
        try:
            cliente = Clientes.objects.get(id_cliente=id_cliente)
            if form.is_valid():
                form.save()

                if cliente.id_estado.estado == 'Inactivo':
                    estado_activo = Estados.objects.get(estado='Activo')
                    cliente.id_estado = estado_activo
                    cliente.save()
                return redirect('../')
            else:
                print('Los errores del formulario son: ', form.errors)
        except Clientes.DoesNotExist:
            error = 'El ID del cliente no existe.'

            # --- RECONSTRUIR EL CONTEXTO COMO EN LA VISTA PRINCIPAL ---
            query = req.GET.get('q', '').strip()
            if query:
                palabras = query.lower().split()
                inscripciones = InscripcionesRenovaciones.objects.annotate(
                    nombre_completo=Concat(
                        'id_cliente__nombre_cliente',
                        Value(' '),
                        'id_cliente__apellido_cliente'
                    )
                )
                condiciones = Q()
                for palabra in palabras:
                    condiciones |= Q(id_cliente__nombre_cliente__icontains=palabra)
                    condiciones |= Q(id_cliente__apellido_cliente__icontains=palabra)
                    condiciones |= Q(nombre_completo__icontains=palabra)
                resultados = inscripciones.filter(condiciones)
            else:
                resultados = InscripcionesRenovaciones.objects.none()

            if query:
                inscripciones_renovaciones_qs = resultados
            else:
                inscripciones_renovaciones_qs = InscripcionesRenovaciones.objects.all()

            paginator = Paginator(inscripciones_renovaciones_qs, 10)
            page_number = req.GET.get('page')
            page_obj = paginator.get_page(page_number)

            contexto = {
                'error': error,
                'empleado': empleado,
                'inscripciones_renovaciones': page_obj,
                'resultados': resultados,
                'query': query,
                'page_obj': page_obj,
            }
            return render(req, 'admin_pages/inscripciones_renovaciones.html', contexto)
    else:
        form = RenovacionesForm()
    return render(req, 'admin_pages/desplegables/inscripciones_renovaciones/registrar_renovacion.html', {'form': form,'planes': planes,'metodos_pago': metodos_pago,'empleado': empleado})



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
        .exclude(id_rol__rol='Entrenador') \
        .exclude(id_rol__rol='Gerente')

    return render(request, 'admin_pages/desplegables/configuracion/reasignar_inscripciones.html', {
        'empleado_origen': empleado_origen,
        'empleados_destino': empleados_destino
    })


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ejecutar_reasignacion(request):
    if request.method == 'POST':
        origen_id = request.POST.get('origen_id')
        destino_id = request.POST.get('destino_id')

        try:
            origen = Empleados.objects.get(pk=origen_id)
            destino = Empleados.objects.get(pk=destino_id)

            if origen.id_rol.rol == 'Administrador':
                return JsonResponse({'success': False, 'message': 'No se puede eliminar un administrador directamente.'}, status=403)

            inscripciones = InscripcionesRenovaciones.objects.filter(id_empleado=origen)
            if not inscripciones.exists():
                return JsonResponse({'success': False, 'message': 'El empleado no tiene inscripciones asignadas.'}, status=400)

            inscripciones.update(id_empleado=destino)
            origen.delete()

            return JsonResponse({'success': True, 'message': 'Inscripciones reasignadas y empleado eliminado correctamente.'})
        except Empleados.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Empleado no encontrado.'}, status=404)
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)

def actualizar_datos_cliente(request, id_cliente):
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        cliente = get_object_or_404(Clientes, id_cliente=id_cliente)

        # Contraseña
        nueva = request.POST.get('input_contrasena')
        confirmar = request.POST.get('confirmar-contrasena')
        if nueva and nueva == confirmar:
            cliente.contrasena_cliente = nueva

        # Correo
        nuevo_correo = request.POST.get('input_correo')
        if nuevo_correo:
            cliente.correo_cliente = nuevo_correo

        # Teléfono
        nuevo_telefono = request.POST.get('input_telefono')
        if nuevo_telefono:
            cliente.telefono_cliente = nuevo_telefono

        cliente.save()
        return redirect('user/ajustes_cuenta')  # O la vista que tú uses

    return redirect('user/ajustes_cuenta')

def cancelar_membresia(request, cliente_id):
    if request.method == 'POST':
        try:
            cliente = Clientes.objects.get(id_cliente=cliente_id)
            estado_inactivo = Estados.objects.get(estado='Inactivo')
            cliente.id_estado = estado_inactivo
            cliente.save()
            return JsonResponse({'success': True, 'nuevo_estado': estado_inactivo.estado})
        except Clientes.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Cliente no encontrado'})
        except Estados.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Estado "Inactivo" no existe'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)
def perfil_empleado(req, id):
    empleado = Empleados.objects.get(id_empleado = id)
    return render(req, 'admin_pages/desplegables/perfil_empleado.html',{'empleado': empleado})


def verificar_inscripciones(request, id_empleado):
    tiene = InscripcionesRenovaciones.objects.filter(id_empleado_id=id_empleado).exists()
    return JsonResponse({'tiene_inscripciones': tiene}, content_type='application/json')

@csrf_exempt  # Solo si no estás usando el token correctamente
def eliminar_empleado(request, id_empleado):
    if request.method == 'POST':
        try:
            empleado = Empleados.objects.get(pk=id_empleado)

            # Verifica si es entrenador
            if empleado.id_rol.rol == 'Entrenador':
                # Elimina sus relaciones en entrenador_cliente
                EntrenadorCliente.objects.filter(id_entrenador=empleado).delete()
                
            empleado.delete()
            return JsonResponse({'success': True})
        except Empleados.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Empleado no encontrado.'}, status=404)
    return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)
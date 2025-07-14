from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(req):
#     return HttpResponse('Bienvenido a HAMARFIT')

# Index
def index(req):
    return render(req,'index.html')

# Paginas del apartado de 'user'
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



# Paginas del apartado de 'admin'
def clientes(req):
    return render(req, 'admin_pages/clientes.html')

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
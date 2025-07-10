from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse('Bienvenido a HAMARFIT')

def index(req):
    return render(req,'index.html')

def sucursales(req):
    return render(req,'html/user/sucursales.html')

def checkout(req):
    return render(req,'html/user/checkout.html')
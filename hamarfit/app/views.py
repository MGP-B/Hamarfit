from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aplication(req):
    return HttpResponse('Bienvenido a HAMARFIT')

def aplication(req):
    return render(req,'index.html')

def aplication(req):
    return render(req,'html/user/sucursales.html')

# def aplication(req):
#     return render(req,'html/user/checkout.html')
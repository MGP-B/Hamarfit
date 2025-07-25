from django import forms
from models import *

class ClientesForm(models.modelF):
    class Meta:
        model = Clientes
        fields = [
            'nombre_cliente',
            'apellido_cliente',
            'tipo_documento',
            'documento_cliente',
            'correo_cliente',
            
        ]
    


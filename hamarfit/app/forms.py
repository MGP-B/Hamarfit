from django import forms
from .models import *

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nombre_cliente',
            'apellido_cliente',
            'tipo_documento',
            'documento_cliente',
            'correo_cliente',
            'telefono_cliente',
            'direccion_cliente',
            'contrasena_cliente',
            'id_plan',
            'id_sucursal',
        ]


from django import forms
from .models import *

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        # fields = [
        #     'nombre_cliente',
        #     'apellido_cliente',
        #     'tipo_documento',
        #     'documento_cliente',
        #     'correo_cliente',
        #     'telefono_cliente',
        #     'direccion_cliente',
        #     'contrasena_cliente',
        #     'id_plan',
        #     'id_sucursal',
        #     'id_estado',
        # ]
        exclude = ['id_plan', 'id_sucursal', 'id_estado']

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = [
            'nombre_empleado',
            'apellido_empleado',
            'tipo_documento',
            'documento_empleado',
            'correo_empleado',
            'telefono_empleado',
            'direccion_empleado',
            'contratacion_empleado',
            'contrasena_empleado',
            'id_rol',
            'id_sucursal',
        ]
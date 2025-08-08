from django import forms
from .models import *

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        exclude = ['inscripcion', 'id_plan', 'id_sucursal', 'id_estado']

class anadirCliente(forms.ModelForm):
    class Meta:
        model = Clientes
        exclude = ['id_estado']

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
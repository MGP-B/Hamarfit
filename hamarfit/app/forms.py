from django import forms
from .models import *
from django.core.exceptions import ValidationError


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

    def clean_correo_empleado(self):
        correo = self.cleaned_data['correo_empleado']

        # Revisar si el correo ya existe en empleados
        if Empleados.objects.filter(correo_empleado=correo).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Este correo ya esta registrado en el sistema.')
        
        # Revisar si el correo ya existe en clientes
        if Clientes.objects.filter(correo_cliente=correo).exists():
            raise forms.ValidationError('Este correo ya esta registrado en el sistema.')
        
        return correo
class SucursalesForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        fields = [
            'nombre_sucursal',
            'direccion_sucursal',
            'telefono_sucursal',
            'hora_apertura',
            'hora_cierre',
            'imagen',
        ]

class RenovacionesForm(forms.ModelForm):
    class Meta:
        model = InscripcionesRenovaciones
        # fields = [
        #     'id_empleado',
        #     'id_metodo',
        #     'id_plan',
        #     'id_cliente',
        #     'descripcion',
        # ]
        exclude = ['emision']

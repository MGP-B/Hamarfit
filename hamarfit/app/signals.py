from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Clientes)
def crear_inscripcion_cliente(sender, instance, created, **kwargs):
    if created:
        empleado = Empleados.objects.first()
        metodo = MetodosPagos.objects.first()

        InscripcionesRenovaciones.objects.create(
            emision=instance.inscripcion,
            id_empleado=empleado,
            id_metodo=metodo,
            id_plan=instance.id_plan,
            id_cliente=instance,
            descripcion="Inscripción"
        )




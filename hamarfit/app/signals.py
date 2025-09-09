from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Clientes, Empleados, InscripcionesRenovaciones, MetodosPagos
from .locals import get_empleado_id

@receiver(post_save, sender=Clientes)
def crear_inscripcion_cliente(sender, instance, created, **kwargs):
    if created:
        empleado_id = get_empleado_id()
        empleado = Empleados.objects.get(id_empleado=empleado_id) if empleado_id else Empleados.objects.first()
        metodo = MetodosPagos.objects.first()

        InscripcionesRenovaciones.objects.create(
            emision=instance.inscripcion,
            id_empleado=empleado,
            id_metodo=metodo,
            id_plan=instance.id_plan,
            id_cliente=instance,
            descripcion="Inscripción"
        )




# app/locals.py
import threading

_local = threading.local()

def set_empleado_id(empleado_id):
    _local.empleado_id = empleado_id

def get_empleado_id():
    return getattr(_local, 'empleado_id', None)

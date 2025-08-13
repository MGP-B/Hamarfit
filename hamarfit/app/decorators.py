from django.shortcuts import redirect
from functools import wraps

def cliente_required(view_func):
    @wraps(view_func)
    def wrapper(req, *args, **kwargs):
        if not req.session.get('cliente_id'):
            return redirect('admin/login')
        return view_func(req, *args, **kwargs)
    return wrapper

def empleado_required(view_func):
    @wraps(view_func)
    def wrapper(req, *args, **kwargs):
        if not req.session.get('empleado_id'):
            return redirect('admin/login')
        return view_func(req, *args, **kwargs)
    return wrapper
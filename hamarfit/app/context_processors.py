def rol_context(req):
    return {
        'rol': req.session.get('rol'),
        'empleado_id': req.session.get('empleado_id'),
    }
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Beneficios(models.Model):
    id_beneficio = models.AutoField(primary_key=True)
    nombre_beneficio = models.CharField(max_length=100)
    id_plan = models.ForeignKey('Planes', models.DO_NOTHING, db_column='id_plan')

    class Meta:
        managed = False
        db_table = 'beneficios'


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=80)
    apellido_cliente = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=30)
    documento_cliente = models.CharField(max_length=13)
    correo_cliente = models.CharField(max_length=80)
    telefono_cliente = models.CharField(max_length=12)
    direccion_cliente = models.CharField(max_length=200)
    inscripcion = models.DateField(auto_now=True)
    contrasena_cliente = models.CharField(max_length=20)
    id_plan = models.ForeignKey('Planes', models.DO_NOTHING, db_column='id_plan')
    id_sucursal = models.ForeignKey('Sucursales', models.DO_NOTHING, db_column='id_sucursal')
    id_estado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = False
        db_table = 'clientes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=80)
    apellido_empleado = models.CharField(max_length=100)
    tipo_documento = models.CharField(db_column='tipo-documento', max_length=30)  # Field renamed to remove unsuitable characters.
    documento_empleado = models.CharField(max_length=13)
    correo_empleado = models.CharField(max_length=80)
    telefono_empleado = models.CharField(max_length=12)
    direccion_empleado = models.CharField(max_length=200)
    contratacion_empleado = models.DateTimeField()
    contrasena_empleado = models.CharField(max_length=20)
    id_rol = models.ForeignKey('Roles', models.DO_NOTHING, db_column='id_rol')
    id_sucursal = models.ForeignKey('Sucursales', models.DO_NOTHING, db_column='id_sucursal')

    class Meta:
        managed = True
        db_table = 'empleados'


class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10, db_collation='utf8mb4_general_ci')

    class Meta:
        managed = False
        db_table = 'estados'


class InscripcionesRenovaciones(models.Model):
    id_finanza = models.AutoField(primary_key=True)
    emision = models.DateField()
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empleado')
    id_metodo = models.ForeignKey('MetodosPagos', models.DO_NOTHING, db_column='id_metodo')
    id_plan = models.ForeignKey('Planes', models.DO_NOTHING, db_column='id_plan')
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente')
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'inscripciones_renovaciones'


class MetodosPagos(models.Model):
    id_metodo = models.AutoField(primary_key=True)
    metodo = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'metodos_pagos'


class NotaClientes(models.Model):
    id_nota = models.AutoField(primary_key=True)
    nota = models.CharField(max_length=800)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'nota_clientes'


class Permisos(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    permiso = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'permisos'


class Planes(models.Model):
    id_plan = models.AutoField(primary_key=True)
    nombre_plan = models.CharField(max_length=40)
    mensualidad = models.FloatField()

    class Meta:
        managed = False
        db_table = 'planes'


class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'roles'


class RolesPermisos(models.Model):
    id_rol = models.OneToOneField(Roles, models.DO_NOTHING, db_column='id_rol')
    id_permiso = models.OneToOneField(Permisos, models.DO_NOTHING, db_column='id_permiso')

    class Meta:
        managed = False
        db_table = 'roles_permisos'


class Sucursales(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=80)
    direccion_sucursal = models.CharField(max_length=200)
    telefono_sucursal = models.CharField(max_length=12)
    horario = models.CharField(max_length=12)
    imagen = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'sucursales'

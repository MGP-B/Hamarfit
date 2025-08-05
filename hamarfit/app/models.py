# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    inscripcion = models.DateField()
    contrasena_cliente = models.CharField(max_length=20)
    id_plan = models.ForeignKey('Planes', models.DO_NOTHING, db_column='id_plan')
    id_sucursal = models.ForeignKey('Sucursales', models.DO_NOTHING, db_column='id_sucursal')
    id_estado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = True
        db_table = 'clientes'


class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=80)
    apellido_empleado = models.CharField(max_length=100)
    tipo_documento = models.CharField(db_column='tipo-documento', max_length=30)  # Field renamed to remove unsuitable characters.
    documento_empleado = models.CharField(max_length=13)
    correo_empleado = models.CharField(max_length=80)
    telefono_empleado = models.CharField(max_length=12)
    direccion_empleado = models.CharField(max_length=200)
    contratacion_empleado = models.DateField()
    contrasena_empleado = models.CharField(max_length=20)
    id_rol = models.ForeignKey('Roles', models.DO_NOTHING, db_column='id_rol')
    id_sucursal = models.ForeignKey('Sucursales', models.DO_NOTHING, db_column='id_sucursal')

    class Meta:
        managed = False
        db_table = 'empleados'


class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'estados'


class Finanzas(models.Model):
    id_finanza = models.AutoField(primary_key=True)
    emision = models.DateField()
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empleado')
    id_metodo = models.ForeignKey('MetodosPagos', models.DO_NOTHING, db_column='id_metodo')
    id_plan = models.ForeignKey('Planes', models.DO_NOTHING, db_column='id_plan')
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'finanzas'


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

from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID único del usuario")
    nombre = models.CharField(max_length=150, help_text="Nombre completo")
    correo = models.EmailField(max_length=254, unique=True, help_text="Correo electrónico único")
    contraseña = models.CharField(max_length=128, help_text="Contraseña encriptada")

 

class Habitacion(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID único de la habitación")
    num_hab = models.CharField(max_length=10, unique=True, help_text="Número de habitación")
    tipo = models.CharField(max_length=50, help_text="Tipo de habitación (sencilla, doble, suite, etc.)")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la habitación")
    precio_por_noche = models.DecimalField(max_digits=8, decimal_places=2, help_text="Precio por noche")
    estado = models.CharField(max_length=20, default='activo', help_text="Estado (activo/inactivo)")

   

class Reserva(models.Model):
    id = models.AutoField(primary_key=True, help_text="ID único de la reserva")
    usuario = models.ForeignKey(Usuario, verbose_name="Usuario", on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, verbose_name="Habitación", on_delete=models.CASCADE)
    fecha_inicio = models.DateField(help_text="Fecha de inicio de la reserva")
    fecha_fin = models.DateField(help_text="Fecha de fin de la reserva")
    estado_reserva = models.CharField(max_length=20, default='pendiente', help_text="Estado de la reserva (pendiente, confirmada, cancelada)")
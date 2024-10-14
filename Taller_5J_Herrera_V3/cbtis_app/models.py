from django.db import models

# Create your models here.
class Alumno(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido paterno")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    Nombres=models.CharField(max_length=100,verbose_name="Nombres (s)")
    Fecha_Nacimiento=models.DateField(verbose_name="Fecha de Nacimiento",null=False,blank=False)
    Fecha_Ingreso=models.DateField(verbose_name="Fecha de Ingreso",null=False,blank=False)
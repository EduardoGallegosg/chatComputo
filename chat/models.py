from django.db import models

# Create your models here.
class Carreras(models.Model):
    nombre = models.CharField(max_length=80)
    status = models.SmallIntegerField()
    def __str__(self):
        return self.nombre
    
class Persona(models.Model):
    nombre = models.CharField(max_length=80)
    ap_pat = models.CharField(max_length=80)
    ap_mat = models.CharField(max_length=80)
    usu = models.CharField(max_length=80)
    pwd = models.CharField(max_length=80)
    fecha_nac = models.DateField()
    carrera = models.ForeignKey(Carreras,on_delete=models.PROTECT)
    status = models.SmallIntegerField()

    def __str__(self):
        return self.nombre

    
class Mensajes(models.Model):
    txt_mensaje = models.CharField(max_length=200)
    persona = models.ForeignKey(Persona,on_delete=models.PROTECT)
    status = models.SmallIntegerField()

    def __str__(self):
        return self.txt_mensaje
    
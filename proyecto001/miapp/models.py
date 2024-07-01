from django.db import models

# Create your models here.
class Course(models.Model):
    idcourse = models.AutoField(primary_key=True,verbose_name="IdCurso")
    code = models.CharField(max_length=20,verbose_name="Código")
    name = models.CharField(max_length=100,verbose_name="Nombre")
    hour = models.PositiveIntegerField(verbose_name="Horas")
    credits = models.PositiveIntegerField(verbose_name="Creditos")
    state = models.BooleanField(verbose_name="Estado")
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        
    def __str__(self):
        if self.state:
            state = "Con Cupos"
        else:
            state = "Sin Cupos"
        return f"{self.name} ({state})"
        
class Career(models.Model):
    idcareer = models.AutoField(primary_key=True,verbose_name="IdCarrera")
    name = models.CharField(max_length=100,verbose_name="Nombre")
    shortname = models.CharField(max_length=10,verbose_name="NombreCorto")
    image = models.ImageField(upload_to='carreras', default='null',verbose_name="Imagen")
    state = models.BooleanField(verbose_name="Estado")   
    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        
    def __str__(self):
        if self.state:
            state = "Habilitada"
        else:
            state = "No Habilitada"
        return f"{self.name} ({state})"
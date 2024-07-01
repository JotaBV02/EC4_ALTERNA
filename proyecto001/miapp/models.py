from django.db import models

# Create your models here.
class Course(models.Model):
    idcourse = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    hour = models.PositiveIntegerField()
    credits = models.PositiveIntegerField()
    state = models.BooleanField()
 
class Career(models.Model):
    idcareer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=10)
    image = models.ImageField(upload_to='carreras', default='null')
    state = models.BooleanField()   
    
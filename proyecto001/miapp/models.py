from django.db import models

# Create your models here.
class Course(models.Model):
    idcourse = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    hour = models.PositiveIntegerField()
    credits = models.PositiveIntegerField()
    state = models.BooleanField()
    
    
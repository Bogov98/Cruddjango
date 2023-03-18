from django.db import models

# Create your models here.
class Task(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=25)
    descripcion= models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=20,decimal_places=2)
    cantidad= models.CharField(max_length=50)
    categoria= models.CharField(max_length=25)

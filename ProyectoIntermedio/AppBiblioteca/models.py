from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    sinopsis = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.titulo} - {self.autor}'
    
class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
    
class Sector(models.Model):
    color = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    cupo = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.color}'
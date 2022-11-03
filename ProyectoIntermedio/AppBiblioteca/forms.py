from django import forms

class Libros(forms.Form):
    titulo = forms.CharField(max_length=50)
    sinopsis = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=50)
    codigo_libro = forms.IntegerField()
    
class Socios(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    fecha_nac = forms.DateField()
    codigo_socio = forms.IntegerField()
    
class Sectores(forms.Form):
    color = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)
    cupo = forms.IntegerField()
    codigo_sector = forms.IntegerField()
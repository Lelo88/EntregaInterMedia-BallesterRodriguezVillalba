from django.shortcuts import render, redirect
from .models import Socio, Sector, Libro
from .forms import Libros, Socios, Sectores

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def libros(request):
    
    libro = Libro.objects.all()
    
    return render(request, 'listado_libros.html',{'lista_libros': libro})

def sectores(request):
    
    sector = Sector.objects.all()

    return render(request, 'listado_sectores.html', {'lista_sectores': sector})

def socios(request):
    
    socio = Socio.objects.all()
    
    return render(request, 'listado_socios.html', {'lista_socios': socio})

def form_libros(request):
    
    if request.method == "POST":
        libros = Libros(request.POST)
        
        if libros.is_valid():
            info_libros = libros.cleaned_data
            libro = Libro(titulo=info_libros['titulo'], sinopsis=info_libros['sinopsis'], autor=info_libros['autor'])
            libro.save()
            
            return redirect('ListadoLibros')
        
    else:
        libros = Libros()
    
    return render(request, 'formularioLibros.html', {'libros': libros})


def form_sectores(request):
    
    if request.method=='POST': 
        sectores = Sectores(request.POST)
        
        if sectores.is_valid():
            info_sectores = sectores.cleaned_data
            sector = Sector(color=info_sectores['color'], nombre=info_sectores['nombre'], cupo=info_sectores['cupo'])
            sector. save()
            
            return redirect('ListadoSectores')

    else:
        sectores = Sectores()
        
    return render(request, 'formularioSectores.html',{'sectores': sectores})

def form_socios(request):
    
    if request.method == 'POST':
        socios = Socios(request.POST)
        
        if socios.is_valid():
            info_lectores = socios.cleaned_data
            lector = Socio(nombre=info_lectores['nombre'], apellido=info_lectores['apellido'], fecha_nac=info_lectores['fecha_nac'])
            lector.save()
            
            return redirect('ListadoSocios')
    
    else:
        lectores = Socios()
        
    return render(request, 'formularioLectores.html', {'socios': socios})

def form_inicial(request):
    pass
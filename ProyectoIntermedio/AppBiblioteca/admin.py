from django.contrib import admin
from .models import Libro, Sector, Socio
# Register your models here.

admin.site.register(Libro)
admin.site.register(Sector)
admin.site.register(Socio)
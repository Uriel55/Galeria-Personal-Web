from django.contrib import admin

# Register your models here.
#10 Registrar los modelos en la base de datos
from .models import Imagen, Categoria

admin.site.register(Categoria)
admin.site.register(Imagen)
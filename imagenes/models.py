from django.db import models

# Create your models here.

#9 Crear modelos de las Imágenes para la base de datos
#9 Realizar migraciones a la base de datos después de crear el modelo.
#10 También llegado a este paso; crear superusuario, django admin
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.nombre
    
class Imagen(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(null=False, blank=False)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.descripcion
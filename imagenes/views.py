from django.shortcuts import render, redirect
from .models import Categoria, Imagen

# Create your views here.
#2 Configurar vistas de las páginas del sitio. Proceder a crear archivo "urls.py" en la aplicación
def galeria(request):
    categoria = request.GET.get('categoria')  #22 Recibir la categoría por medio de la URL
    
    #23 Consultar todas las categorías si no hay categoría especifica recibida, para mostrarlas en la galería
    if categoria == None:
        imagenes = Imagen.objects.all()   #14 Tomar todas las imagenes de la base de datos para pasarlas a la página 
    #23 Consultar las imagenes pertenecientes a la categoría recibida, para mostrarlas en la galería
    else:
        imagenes = Imagen.objects.filter(categoria__nombre=categoria)
    
    categorias = Categoria.objects.all()   #13 Tomar las categorías de la base de datos para mostrarlas en la página inicial
    contexto = {'categorias': categorias, 'imagenes': imagenes}
    
    return render(request, 'imagenes/galeria.html', contexto)

def verImagen(request, pk):
    imagen = Imagen.objects.get(id=pk)
    return render(request, 'imagenes/imagen.html', {'imagen': imagen})

def agregarImagen(request):
    categorias = Categoria.objects.all()   #16 Tomar todas las categorías existentes para mostrarlas en la selección de categoría para la imagen nueva
    
    if request.method == 'POST':
        datos = request.POST    #20 Recibir los datos ingresados
        imagen = request.FILES.get('imagen')  #20 Recibir el archivo de imagen ingresado

        if datos['categoria'] != 'none':      #21 Asignar categoría seleccionada
            categoria = Categoria.objects.get(id=datos['categoria'])
            
        elif datos['categoria_nueva'] != "":   #21 Asignar categoría creada
            categoria, creada = Categoria.objects.get_or_create(nombre=datos['categoria_nueva'])
            
        else:     #21 Asignar categoría vacía, imagen sin categoría
            categoria = None
        
        
            #21 Crear imagen nueva en la base con los datos recibidos
        imagen = Imagen.objects.create(
            categoria = categoria,
            descripcion = datos['descripcion'],
            imagen = imagen,
        )
        
        #21 Redireccionar a la galería principal una vez subida la nueva imagen
        return redirect('galeria')
            
    
    contexto = {'categorias': categorias}
    
    return render(request, 'imagenes/agregar.html', contexto)


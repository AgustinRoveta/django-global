from django.shortcuts import render, redirect, get_object_or_404
from inventario.forms import FormProducto
from inventario.models import  Productos,Categorias
from django.contrib.auth.decorators import login_required

"""GET buscar informacion"""
# Create your views here.


def listarProductos(req):
    productos=Productos.objects.all() #SELECT * FROM productos
    categorias= Categorias.objects.all()#SELECT * FROM categorias
    formulario= FormProducto()

    #no olvidar incluir en el contexto
    contexto={"productos":productos, "categorias":categorias, "formulario":formulario}#el string es el tipo de nombre que le voy a dar para renderizarlo en el html, el any va a ser cualquier objeto que le quiera pasar, el objeto va a ser un diccionario 
    return render(req,'index.html',contexto)

#Eliminar un productos
#dentro de productos voy a buscar un objeto en particular,cuyo id sea igual al id que le acabo de pasar, buscando dentro del listado de productos el objeto cuyo id sea igual al que le pase 

@login_required
def eliminarProducto(req,id):
    producto=Productos.objects.get(id=id)
    producto.delete()
    return redirect('base')

#Usaremos la funcion para RECIBIR el producto a editar y GUARDAR el producto editado

@login_required
def editarProducto(req,id):
    #producto= Productos.objects.get(id=id)
    #lista_categorias= Categorias.objects.all()
    producto=get_object_or_404(Productos,id=id)
    if req.method=="GET":
        formulario= FormProducto(instance=producto)
        contexto={"producto": producto,"formulario": formulario}
        return render(req, 'editar.html', contexto)
    elif req.method =="POST":
    # nombre_nuevo=req.POST["nombre"]
    # precio_nuevo=req.POST["precio"]
    # stock_nuevo=req.POST["stock"]
    # id_categoria_nueva=req.POST["categoria"]
    # categoria_nueva= Categorias.objects.get(id=id_categoria_nueva)
    # producto.nombre=nombre_nuevo
    # producto.precio=precio_nuevo
    # producto.stock=stock_nuevo
    # producto.categoria_fk=categoria_nueva #guardamos instancias, por lo general en la fk se guardan instancias
    # #necesito SI O SI volver a guardar el producto
    # producto.save()
        formulario=FormProducto(req.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
        return redirect('base')

@login_required
def crearProducto(req):
#    nombre_post= req.POST["nombre"]
#    precio_post=req.POST["precio"]
#    stock_post=req.POST["stock"]
#    categoria_id=req.POST["categoria"]
#    categoria_instance= Categorias.objects.get( id=categoria_id) 
#    producto= Productos(nombre=nombre_post, precio=precio_post,stock=stock_post,categoria_fk=categoria_instance)
#    producto.save()  #EL SAVE ES OBLIGATORIO PARA GUARDAR EL PRODUCTO
#? Form de creacion de producto
    form_producto=FormProducto(req.POST)
    if form_producto.is_valid():
        form_producto.save()
    return redirect('base')


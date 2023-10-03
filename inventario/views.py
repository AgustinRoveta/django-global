from django.shortcuts import render, redirect, HttpResponse
from inventario.models import Productos
"""GET buscar informacion"""
# Create your views here.
def listarProductos(req):
    productos=Productos.objects.all() #SELECT * FROM productos
    contexto={'productos':productos}#el string es el tipo de nombre que le voy a dar para renderizarlo en el html, el any va a ser cualquier objeto que le quiera pasar, el objeto va a ser un diccionario 
    return render(req,'index.html',contexto)
#Eliminar un productos
#dentro de productos voy a buscar un objeto en particular,cuyo id sea igual al id que le acabo de pasar, buscando dentro del listado de productos el objeto cuyo id sea igual al que le pase 
def eliminarProducto(req,id):
    producto=Productos.objects.get(id=id)
    producto.delete()
    return redirect('base')

#Usaremos la funcion para RECIBIR el producto a editar y GUARDAR el producto editado
def editarProducto(req,id):
    producto= Productos.objects.get(id=id)
    if req.method=="GET":
        contexto={"producto": producto}
        return render(req, 'editar.html', contexto)
    elif req.method =="POST":
        nombre_nuevo=req.POST["nombre"]
        precio_nuevo=req.POST["precio"]
        stock_nuevo=req.POST["stock"]
        
        producto.nombre=nombre_nuevo
        producto.precio=precio_nuevo
        producto.stock=stock_nuevo
        #necesito SI O SI volver a guardar el producto
        producto.save()
        return redirect('base')

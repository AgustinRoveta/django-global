from django.urls import path

from inventario.views import editarProducto, eliminarProducto, listarProductos  
urlpatterns = [
    path('', listarProductos, name="base"),

    path('eliminar/<id>', eliminarProducto, name="eliminar"),  
    # eliminarProducto es la funcion encargada de eliminar, 
    # el name identificara como se llamara al metodo dentro del contexto,
    # asi sera llamado en el momento de ejecución 
    #el <id> quiere decir que se le pasara un id a través de un parametro
path('editar/<id>', editarProducto, name="editar")  
]
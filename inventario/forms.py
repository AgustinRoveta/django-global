#Aca vamos a crear nuestro form para hacer todo mas EFICIENTE en el manejo de Django
#?Ventaja: Mayor velocidad de procesamiento de campos necesarios, al igual que el uso de VALIDACIONES propias que tiene el form
#!Desventaja: Los forms requieren que los estilos le sean dados desde css, esto debido a que no tendremos acceso desde el HTML al elemento
#!sera Django el encargado de crear el HTML necesario para que sea renderizado del lado del cliente
from django import forms

from inventario.models import Productos


class FormProducto(forms.ModelForm):
    class Meta:
        error= "Errors Found in your form"
        model = Productos
        fields= '__all__'

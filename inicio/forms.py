from django import forms
from ckeditor.fields import RichTextFormField


class ProductoFormulario(forms.Form):
    title = forms.CharField(label="Título", max_length=50);
    brand = forms.CharField(label="marca", max_length=50);
    image = forms.ImageField(label="imagen", required=False);
    created_at = forms.DateField(label="Fecha de creacion");
    description = RichTextFormField(label="Descripción");
    stock = forms.IntegerField(label="Stock");
    price = forms.DecimalField(label="Precio", decimal_places=2, max_digits=10, );

class CrearProductoFormulario(ProductoFormulario):
   ...
class EditarProductoFormulario(ProductoFormulario):
    ...


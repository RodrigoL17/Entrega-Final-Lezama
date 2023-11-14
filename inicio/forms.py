from django import forms

class ProductoFormulario(forms.Form):
    title = forms.CharField(max_length=50);
    brand = forms.CharField(max_length=50);
    # image = forms.ImageField();
    created_at = forms.DateField();
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':20, "maxlength": 100}));
    stock = forms.IntegerField();
    price = forms.DecimalField(decimal_places=2, max_digits=10, );

class CrearProductoFormulario(ProductoFormulario):
   ...
class EditarProductoFormulario(ProductoFormulario):
    ...


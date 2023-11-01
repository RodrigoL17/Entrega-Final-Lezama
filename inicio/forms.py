from django import forms

class CrearProductoFormulario(forms.Form):
    title = forms.CharField(max_length=50);
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':20, "maxlength": 100}));
    stock = forms.IntegerField();
    price = forms.DecimalField(decimal_places=2, max_digits=10, );

class CrearReviewFormulario(forms.Form):
    rating = forms.IntegerField(min_value=0, max_value=5);
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':20, "maxlength": 100}));
    username = forms.CharField(max_length=50);
    
class CrearCategoryFormulario(forms.Form):
    title = forms.CharField(max_length=50);
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':20, "maxlength": 100}));    
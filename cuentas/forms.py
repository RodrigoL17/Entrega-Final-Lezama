from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta: 
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
 
class FormularioEdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label="Cambiar email", required=False)
    first_name = forms.CharField(label="Cambiar nombre", required=False)
    last_name = forms.CharField(label="Cambiar apellido", required=False)
    biografia = forms.CharField(label="Biografia", max_length=500, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(label="Avatar", required=False)
    
    class Meta: 
        model= User
        fields = ["email", "first_name", "last_name", "biografia", "avatar"]
        
            
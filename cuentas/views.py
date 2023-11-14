from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from cuentas.forms import FormularioDeCreacion, FormularioEdicionPerfil
from cuentas.models import DatosExtra


def login(request):
    formulario = AuthenticationForm()

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.cleaned_data.get("username")
            password = formulario.cleaned_data.get("password")

            user = authenticate(username=user, password=password)

            django_login(request, user)

            DatosExtra.objects.get_or_create(user=request.user)

            return redirect("index")

    return render(request, "cuentas/login.html", {"form": formulario})


def registro(request):
    formulario = FormularioDeCreacion()

    if request.method == "POST":
        formulario = FormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")

    return render(request, "cuentas/registro.html", {"form": formulario})


def perfil(request):
    return render(request, "cuentas/perfil.html")


def editar_perfil(request):
    datos_extra = request.user.datosextra

    formulario = FormularioEdicionPerfil(
        initial={"biografia": datos_extra.biografia, "avatar": datos_extra.avatar},
        instance=request.user,
    )

    if request.method == "POST":
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user, )
        if formulario.is_valid():
            nueva_biografia = formulario.cleaned_data.get("biografia")
            nuevo_avatar = formulario.cleaned_data.get("avatar")

            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
            if nuevo_avatar:
                datos_extra.avatar = nuevo_avatar
                
            datos_extra.save()
            formulario.save()
            return redirect("perfil")

    return render(request, "cuentas/editar_perfil.html", {"form": formulario})


class CambiarPassword(PasswordChangeView):
    template_name = "cuentas/cambiar_password.html"
    success_url = reverse_lazy("perfil")

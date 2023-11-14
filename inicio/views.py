from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from inicio.models import Producto
from inicio.forms import (
    CrearProductoFormulario,
    EditarProductoFormulario,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, "inicio/index.html", {})


class ListadoDeProductos(ListView):
    model = Producto
    context_object_name = "productos"
    template_name = "inicio/productos.html"


def productos(request):
    productos = request.GET.get("search")

    if productos:
        productos_a_mostrar = Producto.objects.filter(title__icontains=productos)
    else:
        productos_a_mostrar = Producto.objects.all()
    return render(request, "inicio/productos.html", {"productos": productos_a_mostrar})


class CrearProducto(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "inicio/crear_producto.html"
    fields = ["title", "brand", "description", "price", "stock", "created_at"]
    success_url = reverse_lazy("productos")


@login_required
def crear_producto(request):
    if request.method == "POST":
        formulario = CrearProductoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            title = info_limpia.get("title")
            brand = info_limpia.get("brand")
            description = info_limpia.get("description")
            price = info_limpia.get("price")
            stock = info_limpia.get("stock")
            created_at = info_limpia.get("created_at")

            producto = Producto(
                title=title,
                brand=brand,
                description=description,
                price=price,
                stock=stock,
                created_at=created_at,
            )
            producto.save()
            return redirect("productos")
        else:
            return render(
                request, "inicio/crear_producto.html", {"form": formulario}
            )
    formulario = CrearProductoFormulario()
    return render(request, "inicio/crear_producto.html", {"form": formulario})


class EliminarProducto(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "inicio/eliminar_producto.html"
    success_url = reverse_lazy("productos")

@login_required
def eliminar_producto(request, producto_id):
    producto_a_eliminar = Producto.objects.get(id=producto_id)
    producto_a_eliminar.delete()
    return redirect("productos")


class EditarProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "inicio/editar_producto.html"
    fields = ["title", "brand", "description", "price", "stock", "created_at"]
    success_url = reverse_lazy("productos")

@login_required
def editar_producto(request, producto_id):
    producto_a_actualizar = Producto.objects.get(id=producto_id)

    if request.method == "POST":
        formulario = EditarProductoFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data

            producto_a_actualizar.title = info_nueva.get("title")
            producto_a_actualizar.brand = info_nueva.get("brand")
            producto_a_actualizar.description = info_nueva.get("description")
            producto_a_actualizar.price = info_nueva.get("price")
            producto_a_actualizar.stock = info_nueva.get("stock")
            producto_a_actualizar.created_at = info_nueva.get("created_at")

            producto_a_actualizar.save()
            return redirect("productos")
        else:
            return render(
                request, "inicio/editar_producto.html", {"form": formulario}
            )
    formulario = EditarProductoFormulario(
        initial={
            "title": producto_a_actualizar.title,
            "brand": producto_a_actualizar.brand,
            "description": producto_a_actualizar.description,
            "price": producto_a_actualizar.price,
            "stock": producto_a_actualizar.stock,
            "created_at": producto_a_actualizar.created_at,
        }
    )
    return render(request, "inicio/editar_producto.html", {"form": formulario})


class DetalleProducto(DetailView):
    model = Producto
    template_name = "inicio/detalle_producto.html"


def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, "inicio/detalle_producto.html", {"producto": producto})


# def reviews(request):
#     reviews = Review.objects.all()
#     return render(request, "inicio/reviews.html", {"reviews": reviews})


# def crear_review(request):
#     if request.method == "POST":
#         formulario = CrearReviewFormulario(request.POST)
#         if formulario.is_valid():
#             info_limpia = formulario.cleaned_data
#             rating = info_limpia.get("rating")
#             description = info_limpia.get("description")
#             username = info_limpia.get("username")

#             review = Review(rating=rating, description=description, username=username)
#             review.save()
#     formulario = CrearReviewFormulario()
#     return render(request, "inicio/crear_review.html", {"formulario": formulario})


# def crear_category(request):
#     if request.method == "POST":
#         formulario = CrearCategoryFormulario(request.POST)
#         if formulario.is_valid():
#             info_limpia = formulario.cleaned_data
#             title = info_limpia.get("title")
#             description = info_limpia.get("description")

#             category = Category(title=title, description=description)
#             category.save()
#     formulario = CrearCategoryFormulario()
#     return render(request, "inicio/crear_category.html", {"formulario": formulario})

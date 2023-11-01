from django.shortcuts import render
from inicio.models import Producto, Review, Category
from inicio.forms import CrearProductoFormulario, CrearReviewFormulario, CrearCategoryFormulario


def index(request):
    return render(request, "inicio/index.html", {})


def productos(request):
    productos = Producto.objects.all()
    return render(request, "inicio/productos.html", {"productos": productos})


def reviews(request):
    reviews = Review.objects.all()
    return render(request, "inicio/reviews.html", {"reviews": reviews})


def crear_producto(request):
    if request.method == "POST":
        formulario = CrearProductoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            title = info_limpia.get("title")
            description = info_limpia.get("description")
            price = info_limpia.get("price")
            stock = info_limpia.get("stock")

            producto = Producto(
                title=title, description=description, price=price, stock=stock
            )
            producto.save()
    formulario = CrearProductoFormulario()
    return render(request, "inicio/crear_producto.html", {"formulario": formulario})


def crear_review(request):
    if request.method == "POST":
        formulario = CrearReviewFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            rating = info_limpia.get("rating")
            description = info_limpia.get("description")
            username = info_limpia.get("username")

            review = Review(rating=rating, description=description, username=username)
            review.save()
    formulario = CrearReviewFormulario()
    return render(request, "inicio/crear_review.html", {"formulario": formulario})

def crear_category(request):
    if request.method == "POST":
        formulario = CrearCategoryFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            title = info_limpia.get("title")
            description = info_limpia.get("description")

            category = Category(title=title, description=description)
            category.save()
    formulario = CrearCategoryFormulario()
    return render(request, "inicio/crear_category.html", {"formulario": formulario})

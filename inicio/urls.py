from django.urls import path
from inicio.views import index, productos, crear_producto, reviews, crear_review, crear_category

urlpatterns = [
    path('', index, name="index"),
    path('productos/', productos, name="productos"),
    path("productos/crear-prodcuto/", crear_producto, name="crear_producto"),
    path("reviews/", reviews, name="reviews"),
    path("reviews/crear-review/", crear_review, name="crear_review"),
    path("categories/crear-category/", crear_category, name="crear_category"),
]
from django.urls import path
from inicio.views import index, productos, crear_producto, eliminar_producto, editar_producto, detalle_producto, ListadoDeProductos, CrearProducto, DetalleProducto, EliminarProducto, EditarProducto

urlpatterns = [
    path('', index, name="index"),
    # path('productos/', productos, name="productos"),
    path("productos/", ListadoDeProductos.as_view(), name="productos"),
    # path("productos/<int:producto_id>/", detalle_producto, name="detalle_producto"),
    path("productos/<int:pk>/", DetalleProducto.as_view(), name="detalle_producto"),
    # path("productos/crear-producto/", crear_producto, name="crear_producto"),
    path("productos/crear-producto/", CrearProducto.as_view(), name="crear_producto"),
    # path("productos/eliminar-producto/<int:producto_id>/", eliminar_producto, name="eliminar_producto"),
    path("productos/eliminar-producto/<int:pk>/", EliminarProducto.as_view(), name="eliminar_producto"),
    # path("productos/editar-producto/<int:producto_id>/", editar_producto, name="editar_producto"),
    path("productos/editar-producto/<int:pk>/", EditarProducto.as_view(), name="editar_producto"),
]
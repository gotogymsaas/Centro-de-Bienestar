from django.urls import path
from .views import ProductFormView, CategoryFormView, ProductListView, CategoryListView

urlpatterns = [
    path(
        "",
        ProductListView.as_view(),
        name="list_product",
    ),
    path(
        "categorias/",
        CategoryListView.as_view(),
        name="list_category",
    ),
    path(
        "agregar/productos",
        ProductFormView.as_view(),
        name="add_product",
    ),
    path(
        "agregar/categorias",
        CategoryFormView.as_view(),
        name="add_category",
    ),
]

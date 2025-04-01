from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)  # Nombre del producto
    description = models.CharField(
        max_length=300, null=True, blank=True
    )  # Descripción detallada
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    stock = models.PositiveIntegerField(default=0)  # Cantidad disponible en inventario
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )  # Categoría del producto
    image = models.ImageField(
        upload_to="products/", null=True, blank=True
    )  # Imagen del producto
    is_active = models.BooleanField(
        default=True
    )  # Indicador de si el producto está activo
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización

    def __str__(self):
        return self.name

    def in_stock(self):
        """
        Verifica si el producto está disponible en inventario.
        """
        return self.stock > 0

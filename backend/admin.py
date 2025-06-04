from django.contrib import admin
from .models import Producto, Pedido, Usuario

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio')
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria',)

admin.site.site_header = "Administración Centro de Bienestar"
admin.site.site_title = "Administrador"
admin.site.index_title = "Bienvenido al Panel de Administración Premium de GoToGym"


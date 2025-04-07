from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Custom admin panel for GoToGym – centrado en bienestar, claridad y gestión eficiente
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active'
    )
    list_filter = (
        'is_staff', 'is_active', 'groups'
    )
    search_fields = (
        'username', 'email', 'first_name', 'last_name'
    )
    ordering = ('username',)

    fieldsets = (
        ("Información de cuenta", {
            'fields': ('username', 'password')
        }),
        ("Datos personales", {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ("Permisos y acceso", {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ("Fechas importantes", {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'first_name', 'last_name',
                'password1', 'password2', 'is_active', 'is_staff', 'groups'
            ),
        }),
    )

    # Traducción de secciones si deseas internacionalizar el panel
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

# Registro del modelo Group con posibilidad futura de personalización
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


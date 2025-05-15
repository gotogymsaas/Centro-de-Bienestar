from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Nombre de la empresa"))
    identifier = models.CharField(
        max_length=100, unique=True, verbose_name=_("Identificador único")
    )
    administrators = models.ManyToManyField(
        User, related_name="managed_companies", verbose_name=_("Administradores")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Fecha de creación")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Última actualización")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")


class Brand(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="brands",
        verbose_name=_("Empresa"),
    )
    name = models.CharField(max_length=255, verbose_name=_("Nombre de la marca"))
    logo = models.ImageField(
        upload_to="brands/logos/", null=True, blank=True, verbose_name=_("Logotipo")
    )
    description = models.TextField(
        null=True, blank=True, verbose_name=_("Descripción de la marca")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Fecha de creación")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Última actualización")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Marca")
        verbose_name_plural = _("Marcas")

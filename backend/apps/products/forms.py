from django import forms
from .models import Product
from .models import Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "stock",
            "category",
            "image",
            "is_active",
        ]
        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Describe el producto"}
            ),
            "price": forms.NumberInput(
                attrs={"step": "0.01", "placeholder": "Precio del producto"}
            ),
            "stock": forms.NumberInput(attrs={"placeholder": "Cantidad en inventario"}),
            "is_active": forms.CheckboxInput(),
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor a 0.")
        return price


##    def save(self, commit=True):
        # Obtener la instancia del producto
  ##      product = super().save(commit=False)

        # Ejemplo: Modificar o agregar lógica antes de guardar
    ##    if not product.description:
      ##      product.description = f"Producto: {product.name}"  # Asignar una descripción genérica si está vacía

        ##if commit:
          ##  product.save()
       ## return product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nombre de la categoría"}),
            "description": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Descripción opcional"}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name.isalpha():
            raise forms.ValidationError(
                "El nombre de la categoría debe contener solo letras."
            )
        return name

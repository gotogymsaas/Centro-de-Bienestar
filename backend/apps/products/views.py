from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.list import ListView
from products.models import Product, Category
from .forms import ProductForm, CategoryForm


class BaseFormView(FormView):
    success_url_name = ""

    def get_success_url(self):
        return reverse_lazy(self.success_url_name)


class ProductFormView(BaseFormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url_name = "list_product"

    def form_valid(self, form):
        form.save()
        print("hola")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Errores en el formulario:", form.errors)
        return super().form_invalid(form)


class CategoryFormView(BaseFormView):
    template_name = "products/add_category.html"
    form_class = ProductForm
    success_url_name = "list_product"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"


class CategoryListView(ListView):
    model = Category
    template_name = "products/list_category.html"
    context_object_name = "categories"

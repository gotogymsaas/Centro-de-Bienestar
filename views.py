from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Document
from .forms import DocumentForm

class DocumentListView(ListView):
    model = Document
    template_name = 'documents/document_list.html'
    context_object_name = 'documents'
    paginate_by = 10  # Opcional: para paginación

class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'documents/document_form.html'
    success_url = reverse_lazy('document_list')


from django.urls import path
from django.views.generic import ListView
from .models import Post

urlpatterns = [
    # Página principal del blog: lista de posts
    path('', ListView.as_view(
        model=Post,
        template_name='blog/post_list.html',
        context_object_name='posts'
    ), name='blog'),
]

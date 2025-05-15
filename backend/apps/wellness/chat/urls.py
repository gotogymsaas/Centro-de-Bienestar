from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('ai_response/', views.ai_response, name='ai_response'),
]


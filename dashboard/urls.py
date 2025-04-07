from django.urls import path
from .views import auth_dashboard

urlpatterns = [
    path('', auth_dashboard, name='auth_dashboard'),
]



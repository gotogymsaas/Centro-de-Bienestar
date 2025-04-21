"""
URL configuration for project_gotogym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
from django.views.generic import TemplateView    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
URL configuration for project_gotogym project.
"""
from django.contrib import admin
from django.urls import path, include, include
from django.views.generic import TemplateView
urlpatterns = [
    path('rosetta/', include('rosetta.urls')),    path('rosetta/', include('rosetta.urls')),    path('rosetta/', include('rosetta.urls')),    # Admin
    path('admin/', admin.site.urls),

    # Páginas estáticas
    path('', TemplateView.as_view(template_name="src/home.html"), name="home"),
    path('productos/', TemplateView.as_view(template_name="src/products.html"), name="list_product"),
    path('pedidos/', TemplateView.as_view(template_name="src/orders.html"), name="my_order"),
    path('bienestar/', TemplateView.as_view(template_name="src/wellness.html"), name="bienestar_dashboard"),
    path('metricas/', TemplateView.as_view(template_name="src/metrics.html"), name="nps_chart"),
    path('gestion/', TemplateView.as_view(template_name="src/gestion.html"), name="gestion_index"),
    path('acerca-de/', TemplateView.as_view(template_name="src/about.html"), name="about"),
    path('contacto/', TemplateView.as_view(template_name="src/contact.html"), name="contact"),
    path('politica-de-privacidad/', TemplateView.as_view(template_name="src/privacy_policy.html"), name="privacy_policy"),
    path('terminos-y-condiciones/', TemplateView.as_view(template_name="src/terms_conditions.html"), name="terms_conditions"),
    path('faq/', TemplateView.as_view(template_name="src/faq.html"), name="faq"),
    path('carreras/', TemplateView.as_view(template_name="src/careers.html"), name="careers"),

    # Autenticación
    path('accounts/', include('django.contrib.auth.urls')),   # login, logout, password_reset, etc.
    path('register/', include('users.urls')),                  # tu vista de registro

    # Apps del proyecto
    path('influencers/', include('influencers.urls')),
    path('cart/', include('shopping_cart.urls')),
    path('blog/', include('blog.urls')),
    path('bienestar/chat/', include('wellness.chat.urls')),
    path('dashboard/', include('dashboard.urls')),
]


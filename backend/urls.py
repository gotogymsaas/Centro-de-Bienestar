
from django.contrib.flatpages import views as flatpages_views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # Ruta para Grappelli
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Esto agrega las rutas de registro, login, etc.
    path('', TemplateView.as_view(template_name="src/home.html"), name="home"),
    path('productos/', TemplateView.as_view(template_name="src/products.html"), name="list_product"),
    path('pedidos/', TemplateView.as_view(template_name="src/orders.html"), name="my_order"),
    path('bienestar/', TemplateView.as_view(template_name="src/wellness.html"), name="bienestar_dashboard"),
    path('bienestar/chat/', include('wellness.chat.urls')),
    path('metricas/', TemplateView.as_view(template_name="src/metrics.html"), name="nps_chart"),
    path('gestion/', TemplateView.as_view(template_name="src/gestion.html"), name="gestion_index"),
    path('acerca-de/', TemplateView.as_view(template_name="src/about.html"), name="about"),
    path('contacto/', TemplateView.as_view(template_name="src/contact.html"), name="contact"),
    path('politica-de-privacidad/', TemplateView.as_view(template_name="src/privacy_policy.html"), name="privacy_policy"),
    path('terminos-y-condiciones/', TemplateView.as_view(template_name="src/terms_conditions.html"), name="terms_conditions"),
    path('faq/', TemplateView.as_view(template_name="src/faq.html"), name="faq"),
    path('blog/', TemplateView.as_view(template_name="src/blog.html"), name="blog"),
    path('carreras/', TemplateView.as_view(template_name="src/careers.html"), name="careers"),
]

urlpatterns += [
    path('pages/<slug:slug>/', flatpages_views.flatpage, name='flatpage'),
]


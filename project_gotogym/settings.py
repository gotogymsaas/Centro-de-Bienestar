import os
from pathlib import Path

# BASE_DIR: ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: Se extrae de variables de entorno para mayor seguridad.
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-default-key")

# DEBUG: Controlado por variable de entorno. En producción, asegúrate de que DEBUG sea False.
DEBUG = os.environ.get("DEBUG", "True") == "True"

# ALLOWED_HOSTS: Define los hosts permitidos. Se configuran a través de una variable de entorno.
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Aplicaciones instaladas



INSTALLED_APPS = [
    # Apps predeterminadas de Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Librerías de UI
    "crispy_forms",
    "crispy_tailwind",

    # Tu app de blog
    "blog",

    # Carrito personalizado
    "shopping_cart",

    # Influencers
    "influencers",

    # Apps del proyecto
    "users",
    "products",
    "orders",
    "service",
    "wellness",
    "metric",
    "gestion",
    "documents",
]




# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project_gotogym.urls"

# Configuración de plantillas

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # ...otros context_processors existentes...
            ],
        },
    },
]


WSGI_APPLICATION = "project_gotogym.wsgi.application"

# Base de datos (SQLite para desarrollo; evalúa migrar a PostgreSQL en producción)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internacionalización
LANGUAGE_CODE = "es-co"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# En producción, define STATIC_ROOT para colectar todos los archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLs de redirección para autenticación
LOGIN_REDIRECT_URL = "role_redirect"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"

# Configuración de Crispy Forms para usar Tailwind (alineado con la identidad de marca)
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# Configuración de Logging (para capturar errores y eventos críticos)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

# Notas:
# - Esta configuración utiliza variables de entorno para SECRET_KEY, DEBUG y ALLOWED_HOSTS, facilitando la transición a producción.
# - Se recomienda revisar y actualizar la base de datos para producción (por ejemplo, migrar a PostgreSQL) y configurar medidas adicionales de seguridad (HTTPS, cookies seguras, etc.).
# - La configuración de Crispy Forms y la estructura de TEMPLATES está alineada con la esencia de marca de GoToGym,
#   que combina lujo deportivo, alta tecnología y bienestar personalizado.

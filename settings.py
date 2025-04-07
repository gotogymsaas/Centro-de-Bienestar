import os
from pathlib import Path

# Define la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuraciones básicas (ajusta según tus necesidades)
SECRET_KEY = 'tu-secret-key-aqui'
DEBUG = True
ALLOWED_HOSTS = []


# Aplicaciones instaladas
INSTALLED_APPS = [
    # Interfaz administrativa mejorada
    'jazzmin',             # Cargar primero para sobrescribir estilos por defecto
    'django.contrib.sites' # Necesario para allauth
    'grappelli',           # Opcional: mejora visual de la interfaz Django Admin

    # Apps de Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # Aplicaciones del proyecto GoToGym
    'users_app',
    'products_app',
    'wellness',
    # Aplicaciones de allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  # Opcional, solo si planeas integrar login social    

    # Puedes agregar más apps aquí, como:
'accounts',   
 # 'orders_app',
    # 'ai_assistant',
]

# Configuración del sitio para flatpages
SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Configuración personalizada para Jazzmin
JAZZMIN_SETTINGS = {
    "site_title": "GoToGym Admin",
    "site_header": "Centro de Bienestar Tecnológico GoToGym",
    "site_brand": "GoToGym",
    "welcome_sign": "🌿 Bienvenido al panel que respira innovación, lujo y bienestar.",
    "site_logo": "images/logo_admin.svg",
    "site_logo_classes": "img-circle shadow-md",
    "site_icon": "images/favicon.ico",

    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["dashboard", "products", "orders", "users", "auth"],

    "topmenu_links": [
        {"name": "Ir al Sitio", "url": "/", "new_window": True},
        {"model": "auth.user"},
        {"name": "Cerrar sesión", "url": "admin:logout"},
    ],

    "usermenu_links": [
        {"name": "Perfil", "url": "admin:auth_user_change", "permissions": ["auth.change_user"]},
        {"name": "Soporte", "url": "/soporte", "new_window": True},
    ],

    "icons": {
        "dashboard": "fas fa-chart-line",
        "auth": "fas fa-users-cog",
        "products": "fas fa-tshirt",
        "orders": "fas fa-box-open",
        "users": "fas fa-user-check",
    },

    "changeform_format": "horizontal_tabs",  # alternativo: collapsible, vertical_tabs
    "language_chooser": True,

    "custom_css": "css/admin_custom.css",
    "custom_js": None,

    "related_modal_active": True,
    "show_ui_builder": False,
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_gotogym.urls'

# Configuración de Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates/src")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'project_gotogym.wsgi.application'

# Configuración de la base de datos: migrando de SQLite a PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gotogym_db',         # Nombre de la base de datos que creaste
        'USER': 'gotogym_user',       # Usuario configurado en PostgreSQL
        'PASSWORD': '123Margarita6',  # Reemplaza 'tu_contraseña' con la contraseña real
        'HOST': 'localhost',          # O el host donde se encuentra PostgreSQL
        'PORT': '5432',               # Puerto por defecto de PostgreSQL
    }
}

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# (Aquí puedes continuar con otras configuraciones, como AUTH_PASSWORD_VALIDATORS, LANGUAGE_CODE, TIME_ZONE, etc.)

AUTH_USER_MODEL = 'accounts.CustomUser'


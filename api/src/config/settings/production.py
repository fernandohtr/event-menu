from .base import *

ADMINS = [("Fernando Toledo", "fernandohtr@gmail.com")]
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = [
    ".localhost",
    ".127.0.0.1",
    ".fernandohtr.com",
]
CSRF_TRUSTED_ORIGINS = [
    "https://cardapio.fernandohtr.com",
    "http://cardapio.fernandohtr.com",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}
STATIC_ROOT = "/staticfiles/"
MEDIA_ROOT = "/mediafiles/"
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "https://cardapio.fernandohtr.com",
    "http://cardapio.fernandohtr.com",
]
SECURE_CROSS_ORIGIN_OPENER_POLICY = None
DJANGO_SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 6  # 518400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True

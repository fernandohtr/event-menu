from .base import *

SECRET_KEY = "django-insecure-0ei*l1m2i+s1rkl56yc_vz8jfiqbv4o03+%ie&zcnl!h8nitz&"
DEBUG = True
ALLOWED_HOSTS = ["*"]
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
CORS_ORIGIN_ALLOW_ALL = True

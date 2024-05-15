from .base import *

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True

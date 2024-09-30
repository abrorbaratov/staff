from .common import *

SECRET_KEY = "django-insecure-9*=iuu3_h5m*r5o2=(w4&(q+eidbqk6_f^q)a45_3jj8v^n((q"

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "PORT": 5434,
        "NAME": "staff",
        "USER": "postgres",
        "PASSWORD": "1",
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

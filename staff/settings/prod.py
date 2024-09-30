from .common import *
import dj_database_url

SECRET_KEY = "django-insecure-9*=iuu3_h5m*r5o2=(w4&(q+eidbqk6_f^q)a45_3jj8v^n((q"

host_name = env("HOST_NAME")
front_host = env("front_host")

DEBUG = False

ALLOWED_HOSTS = [f"{host_name}"]

DATABASES = {}

DATABASES["default"] = dj_database_url.parse(env("DATABASE_URL"))

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    f"https://{front_host}",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    f"{host_name}",
]

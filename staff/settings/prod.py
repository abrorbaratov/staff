from .common import *
import dj_database_url

SECRET_KEY = env("SECRET_KEY")

host_name = env("HOST_NAME")
front_host = env("front_host")

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {}

DATABASES["default"] = dj_database_url.parse(env("DATABASE_URL"))

CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://0.0.0.0:8080",
    "http://0.0.0.0",
    f"https://{front_host}",
    f"https://{host_name}",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    f"{host_name}",
]

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Database

if env("LOCAL_DEV_PHASE") == "data_modeling":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
elif env("LOCAL_DEV_PHASE") == "develop":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": env("PSQL_NAME"),
            "USER": env("PSQL_USER"),
            "PASSWORD": env("PSQL_PASSWORD"),
            "HOST": env("PSQL_HOST"),
            "PORT": env("PSQL_PORT"),
        }
    }

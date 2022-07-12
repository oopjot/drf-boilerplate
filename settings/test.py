from settings.base import *  # noqa

ENVIRONMENT = "test"

API_DOMAIN = "localhost:8000"
API_URL = f"https://{API_DOMAIN}"
API_ENTRYPOINT = f"{API_URL}/v1/"

# let's speed up tests a little
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

USE_TZ = False

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
FROM_EMAIL = "no-reply@test.com"

SECRET_KEY = "test"

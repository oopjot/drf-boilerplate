from settings.base import *
import socket

ENVIRONMENT = "local"

DEBUG = True

# for django_debug_toolbar running in docker container
# in order to set internal ips correctly
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

CORS_ORIGIN_WHITELIST = ["http://localhost:3000", "http://localhost:7000"]

# let's speed up tests a little
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

from os import getenv

DEBUG = getenv("DEBUG", 'true').lower() == 'true'

if DEBUG:
    from .dev import *
else:
    from .production import *


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.api',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken'
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}


MQTT_USER = getenv("MQTT_USER")
MQTT_PSW = getenv("MQTT_PSW")
MQTT_HOST = getenv("MQTT_HOST", 'localhost')
MQTT_PORT = int(getenv("MQTT_PORT", 1883))
MQTT_KEEP_ALIVE = int(getenv("MQTT_KEEP_ALIVE", 120))

from os import getenv

DEBUG = getenv("DEBUG", 'true').lower() == 'true'  # If DEBUG is not set, default to True (development mode)

if DEBUG:  # If DEBUG is True, use the dev settings
    from .dev import *
else:  # If DEBUG is False, use the production settings
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


# MQTT Settings
MQTT_USER = getenv("MQTT_USER")
MQTT_PSW = getenv("MQTT_PSW")
MQTT_HOST = getenv("MQTT_HOST", 'localhost')
MQTT_PORT = int(getenv("MQTT_PORT", 1883))
MQTT_KEEP_ALIVE = int(getenv("MQTT_KEEP_ALIVE", 120))

from GeoLoc.settings.base import *
import dj_database_url
# production settings here ...

# Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_EMAIL_TO = ["shivam2012@mailinator.com"]
EMAIL_HOST_USER = "postmaster@sandboxb8649c67dad0414f93072e865827a80c.mailgun.org"
EMAIL_HOST_PASSWORD = "e98b6c20c39c147729d8779f3e5dca57-d5e69b0b-6b7ff0ea"
SECRET_KEY = 'h^xwxv@cgq5m2ue#(y861#_7q4)0jme#+jz!xayo8&6cn@vbc2'


DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
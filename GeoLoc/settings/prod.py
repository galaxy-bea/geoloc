from GeoLoc.settings.base import *
import dj_database_url
# production settings here ...

# Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_EMAIL_TO = ["stabey@gmail.com"]
EMAIL_HOST_USER = "postmaster@mg.wordwideweb.info"
EMAIL_HOST_PASSWORD = "0b67545fd99bcdfbd0188849ef9397ff-2fbe671d-311eef58"
SECRET_KEY = 'h^xwxv@cgq5m2ue#(y861#_7q4)0jme#+jz!xayo8&6cn@vbc2'

if os.environ.get('DJANGO_PRODUCTION'):
  from pathlib import Path
  DATABASES['default'] = dj_database_url.config()
  DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
else:
  DATABASES = {
      'default': {
          'ENGINE': 'django.contrib.gis.db.backends.postgis',
          'NAME': "geoloc",
          'USER': "postgres",
          'HOST': "localhost",
          'PORT': "5432",
          'PASSWORD': "9999"
      },
  }

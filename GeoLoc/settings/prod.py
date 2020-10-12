from GeoLoc.settings.base import *
import dj_database_url
# production settings here ...

# Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_EMAIL_TO = ["stabey@gmail.com"]
EMAIL_HOST_USER = "postmaster@sandbox0a70599ca2d2475686f5142d24c4d49c.mailgun.org"
EMAIL_HOST_PASSWORD = "61159938a0e7241ed04d83bc1e3f8a70-2fbe671d-c726a4bf"
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
          'PASSWORD': "1234"
      },
  }
from GeoLoc.settings.base import *
import dj_database_url
# production settings here ...

# Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_EMAIL_TO = ["shivam2012@mailinator.com"]
EMAIL_HOST_USER = "postmaster@sandboxa9a9c15061884f7aa6cb8a74c1e9d8ea.mailgun.org"
EMAIL_HOST_PASSWORD = "0d9e8f149485a73073c70211b441f933-aff2d1b9-138fb0d5"
SECRET_KEY = 'h^xwxv@cgq5m2ue#(y861#_7q4)0jme#+jz!xayo8&6cn@vbc2'

if os.environ.get('DJANGO_PRODUCTION'):
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
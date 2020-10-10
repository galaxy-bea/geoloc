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
  from pathlib import Path
  DATABASES['default'] = dj_database_url.config()
  DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
  PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')

  sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))


  # Build paths inside the project like this: BASE_DIR / 'subdir'.
  BASE_DIR = Path(__file__).resolve().parent.parent


  # Quick-start development settings - unsuitable for production
  # See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = 'h^xwxv@cgq5m2ue#(y861#_7q4)0jme#+jz!xayo8&6cn@vbc2'

  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = True

  ALLOWED_HOSTS = ['*']


  # Application definition

  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]

  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'whitenoise.middleware.WhiteNoiseMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ]

  ROOT_URLCONF = 'GeoLoc.urls'

  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]

  WSGI_APPLICATION = 'GeoLoc.wsgi.application'

  AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
  ]


  # Internationalization
  # https://docs.djangoproject.com/en/3.1/topics/i18n/

  LANGUAGE_CODE = 'en-us'

  TIME_ZONE = 'UTC'

  USE_I18N = True

  USE_L10N = True

  USE_TZ = True


  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/3.1/howto/static-files/
  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


  STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
  STATIC_URL = '/static/'

  STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'static'),
  ]

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
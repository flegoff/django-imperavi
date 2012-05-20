# Local settings for django_imperavi project.
LOCAL_SETTINGS = True
from settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'imperavi',  # Or path to database file if using sqlite3.
        'USER': 'postgres',                             # Not used with sqlite3.
        'PASSWORD': 'postgres',                         # Not used with sqlite3.
        'HOST': 'localhost',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sfx8sn=wd51(qw39jo4j@18xjh1i!tf8qot2upw_89cccm-y^%'

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

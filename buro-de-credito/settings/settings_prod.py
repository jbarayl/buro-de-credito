#encoding:utf-8
from .settings import *
#Define developer-spesific settings
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'buro_db',                      # Or path to database file if using sqlite3.
        'USER': 'admin_user',                      # Not used with sqlite3.
        'PASSWORD': 'admin',                  # Not used with sqlite3.
    }
}
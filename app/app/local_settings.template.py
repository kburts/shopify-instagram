## Settings template file

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'mysecretkey'

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.hostname.com.',
                 '.hostname.com.']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

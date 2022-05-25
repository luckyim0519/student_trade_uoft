
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'root',
        'PASSWORD': 'lucky',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

SECRET_KEY = 'django-insecure-w$pp#)rdmtpdj7xs5srf@uzns1_nc*19^g-plg2-0)5@ty#a$_'
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'muyibaba',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'MUyibaba',
        'PORT': '5432'
    }
}
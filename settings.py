# mysite/settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# mysite/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
# mysite/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com', '.amazonaws.com']
py -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
# .env
SECRET='paste_your_generated_secret_key_here'
# mysite/settings.py
import os

SECRET_KEY = os.getenv('SECRET')

# ...

ALLOWED_HOSTS = [os.getenv('PROJECT_DOMAIN') + ".glitch.me"]
# mysite/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
python manage.py migrate

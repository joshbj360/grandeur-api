from ._base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config(default=get_secret('DATABASE_URL'))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEBUG = False
ALLOWED_HOSTS = [
    "",
]

from decouple import config
from .base import *

# 'django-insecure-96c6wq=a5x93ef8hn@s+cbi&y2#by8f!o!eavt^y2#9vjg=e!u'
SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

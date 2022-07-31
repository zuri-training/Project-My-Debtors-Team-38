from decouple import config
from .base import *


SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

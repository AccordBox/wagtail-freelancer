import os

from .base import *

env = os.environ.copy()

DEBUG = False

SECRET_KEY = env['SECRET_KEY']

ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')

try:
    from .local import *
except ImportError:
    pass

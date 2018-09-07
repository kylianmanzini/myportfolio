from .base import *

DEBUG = False

ALLOWED_HOSTS = ['kylianmanzini.pythonanywhere.com'] 

try:
    from .local import *
except ImportError:
    pass

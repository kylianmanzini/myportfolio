from .base import *

DEBUG = False

ALLOWED_HOSTS = ['kylianmanzini.pythonanywhere.com'] 

SECRET_KEY = '01xxb#e2)ubqvwyip9hu0xi6(*(rla8)s)5#663u@oj^eg3q2q'

try:
    from .local import *
except ImportError:
    pass

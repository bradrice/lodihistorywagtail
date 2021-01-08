from .base import *
import json


DEBUG = False

try:
    from .local import *
except ImportError:
    pass

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [
    '.lodiharrisvillehistorical.org'
    ] 

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": MAILGUNAPIKEY,
    "MAILGUN_SENDER_DOMAIN": EMAILHOST,  # your Mailgun domain, if needed
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = 'admin@oh-joy.org'
SERVER_EMAIL = 'admin@oh-joy.org'
EMAIL_HOST = EMAILHOST
EMAIL_PORT = SMTPPORT
EMAIL_HOST_USER = EMAILUSER
EMAIL_HOST_PASSWORD = EMAILPASSWORD
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
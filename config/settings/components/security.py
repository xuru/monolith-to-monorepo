from config.settings import env


# Security
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/topics/security/


"""
Do read:

    1. https://docs.djangoproject.com/en/3.1/ref/settings/#sessions
    2. https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
"""
SESSION_COOKIE_AGE = env.int('SESSION_COOKIE_AGE', default=1209600)  # Default - 2 weeks in seconds
SESSION_COOKIE_HTTPONLY = env.bool('SESSION_COOKIE_HTTPONLY', default=True)
SESSION_COOKIE_NAME = env('SESSION_COOKIE_NAME', default='sessionid')
SESSION_COOKIE_SAMESITE = env('SESSION_COOKIE_SAMESITE', default='Lax')
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)

CSRF_USE_SESSIONS = env.bool('CSRF_USE_SESSIONS', default=True)

# CORS settings
# ------------------------------------------------------------------------------
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True

# These two combined can restrict access to the backend by host or CIDR
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*", "localhost", "mtomproxy", "0.0.0.0", "127.0.0.1", "10.0.2.2"])

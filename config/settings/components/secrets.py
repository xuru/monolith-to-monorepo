from config.settings import env

# Secret key
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# ------------------------------------------------------------------------------
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="enGEi8v1E30whLBgdN1qibPFhv7VU9GM48kB3woTwJ4MvAMCqMrT3PB7lLSacW49",
)

# Cache stuff

from config.settings.utils import env

# uses CACHE_URL environment variable (which should be automatically generated in terraform for cloud environments)
CACHES = {
    "default": env.cache(default="redis://redis:6379/1?client_class=django_redis.client.DefaultClient")
}

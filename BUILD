poetry_requirements(
    name="req",
    module_mapping={
        "django-oauth-toolkit": ["oauth2_provider"],
        "django-webpack-loader": ["webpack_loader"],
        "factory-boy": ["factory"],
        "GitPython": ["git"],
        "psycopg2-binary": ["psycopg2"],
        "setuptools": ["pkg_resources"],
        "plaid-python": ["plaid"],
        "polygon-api-client": ["polygon"],
        "polygon-api-client": ["polygon"],
        "django_redis": ["redis"],
        "django-auditlog": ["auditlog"],
        "django-phonenumber-field": ["phonenumber_field"],
        "django-opensearch-dsl": ["django_opensearch_dsl"],
        "django-waffle": ["waffle"],
        "django-bulk-sync": ["bulk_sync"],
        "python-redis-lock": ["redis_lock"],
        "django-timescaledb": ["timescale"],
        "django-cache-memoize": ["cache_memoize"],
        "django-ordered-model": ["ordered_model"],
        "analytics-python": ["analytics"],
        "python-phonenumbers": ["phonenumbers"],
        "django-push-notifications": ["push_notifications"],
        "django-advanced-filters": ["advanced_filters"],
        "drf-jwt": ["rest_framework_jwt"],
    }
)

python_sources(
    name="root",
    dependencies=[":req"],
    sources=['*.py', '**/*.py',  "!**/test_*.py", "!**/conftest.py", '!conftest.py']
)

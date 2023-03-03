import django_filters

from mtom.users.models import User


class BaseUserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ("id", "email", "is_admin")

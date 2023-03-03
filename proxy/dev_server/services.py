from mtom.users.models import User
from proxy.dev_server.models import UserProxyRegister


def dev_server_enable_for_user(user: User):
    UserProxyRegister.objects.get_or_create(user=user)

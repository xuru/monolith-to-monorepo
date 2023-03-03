from proxy.dev_server.models import UserProxyRegister


def dev_server_user_is_proxy_user(user):
    return UserProxyRegister.objects.filter(user=user).exists()
